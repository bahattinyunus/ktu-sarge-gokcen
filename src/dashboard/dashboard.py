import streamlit as st
import pandas as pd
import time
import os
import plotly.express as px

st.set_page_config(
    page_title="Teknofest Rocket Mission Control",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Teknofest 2026 - Mission Control Center")

# Sidebar for status
st.sidebar.header("Connection Status")
status_indicator = st.sidebar.empty()

# Main layout
col1, col2, col3 = st.columns(3)
with col1:
    alt_metric = st.empty()
with col2:
    vel_metric = st.empty()
with col3:
    status_metric = st.empty()

chart_placeholder = st.empty()

def load_data():
    if os.path.exists("telemetry_log.csv"):
        try:
            return pd.read_csv("telemetry_log.csv")
        except:
            return pd.DataFrame()
    return pd.DataFrame()

# Auto-refresh loop
while True:
    df = load_data()
    
    if not df.empty:
        status_indicator.success("Receiving Telemetry 🟢")
        
        last_row = df.iloc[-1]
        
        # Update metrics
        alt_metric.metric("Altitude (m)", f"{last_row['altitude']:.1f} m", delta=f"{df['altitude'].diff().iloc[-1]:.1f}")
        vel_metric.metric("Velocity (m/s)", f"{last_row['velocity']:.1f} m/s", delta=f"{df['velocity'].diff().iloc[-1]:.1f}")
        status_metric.metric("Flight Phase", last_row['status'])

        # Charts
        with chart_placeholder.container():
            col_graph1, col_graph2 = st.columns(2)
            
            with col_graph1:
                st.subheader("Altitude Profile")
                st.line_chart(df, x="timestamp", y="altitude")
                
            with col_graph2:
                st.subheader("3D Trajectory (Live)")
                if 'pos_x' in df.columns and 'pos_y' in df.columns:
                    fig = px.line_3d(df, x='pos_x', y='pos_y', z='altitude', 
                                   title='Rocket Flight Path',
                                   labels={'pos_x': 'Drift X', 'pos_y': 'Drift Y', 'altitude': 'Altitude'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Waiting for 3D data...")
    else:
        status_indicator.warning("Waiting for Data... 🔴")
        st.info("Start the simulation using `make run-telemetry`")

    time.sleep(0.5)
