import streamlit as st
import pandas as pd
import time
import os
import sys
import plotly.express as px

# Add project root to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  

st.set_page_config(
    page_title="Teknofest Rocket Mission Control",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Teknofest 2026 - Mission Control Center")

# Sidebar for status
st.sidebar.header("Connection Status")
status_indicator = st.sidebar.empty()

st.sidebar.markdown("---")
st.sidebar.header("🔥 Fire Control")
from src.telemetry import commander

if st.sidebar.button("ARM ROCKET 🛡️"):
    commander.arm_rocket()
    st.sidebar.warning("Rocket ARMED!")

if st.sidebar.button("LAUNCH 🚀"):
    commander.launch_rocket()
    st.sidebar.error("LAUNCH SEQUENCE INITIATED!")

if st.sidebar.button("DEPLOY CHUTE 🪂"):
    commander.deploy_chute()
    st.sidebar.info("Recovery Initiated.")

if st.sidebar.button("RESET SIM 🔄"):
    commander.reset_simulation()
    st.sidebar.success("Simulation Reset.")

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

        # --- Kalman Filter Application ---
        try:
            from src.algorithms.kalman import KalmanFilter1D
            kf = KalmanFilter1D(initial_value=df['altitude'].iloc[0])
            df['filtered_altitude'] = df['altitude'].apply(lambda x: kf.update(x))
        except Exception as e:
             # st.error(f"Filter Error: {e}")
             df['filtered_altitude'] = df['altitude'] # Fallback
        # ---------------------------------

        # Charts
        with chart_placeholder.container():
            col_graph1, col_graph2 = st.columns(2)
            
            with col_graph1:
                st.subheader("Altitude Analysis (Kalman Filter)")
                # Create a comparison chart
                chart_data = df[['timestamp', 'altitude', 'filtered_altitude']].copy()
                st.line_chart(chart_data, x="timestamp", y=["altitude", "filtered_altitude"], color=["#FF0000", "#00FF00"])
                
            with col_graph2:
                st.subheader("3D Trajectory (Live)")
                if 'pos_x' in df.columns and 'pos_y' in df.columns:
                    fig = px.line_3d(df, x='pos_x', y='pos_y', z='altitude', 
                                   title='Rocket Flight Path',
                                   labels={'pos_x': 'Drift X (m)', 'pos_y': 'Drift Y (m)', 'altitude': 'Altitude (m)'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Waiting for 3D data...")
        
        # GPS Map
        st.subheader("📍 Live GPS Tracking (Tuz Gölü)")
        if 'gps_lat' in df.columns and 'gps_long' in df.columns:
            map_df = df[['gps_lat', 'gps_long']].dropna()
            map_df.columns = ['lat', 'lon'] # Streamlit requires 'lat' and 'lon' column names
            st.map(map_df.tail(50)) # Show path (trail)
        else:
            st.warning("Waiting for GPS data...")
    else:
        status_indicator.warning("Waiting for Data... 🔴")
        st.info("Start the simulation using `make run-telemetry`")

    time.sleep(0.5)
