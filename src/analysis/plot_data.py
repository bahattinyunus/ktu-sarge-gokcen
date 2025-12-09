import matplotlib.pyplot as plt
import csv
import os

def plot_flight_data(log_file="telemetry_log.csv"):
    if not os.path.exists(log_file):
        print(f"❌ Error: {log_file} not found. Run simulation first!")
        return

    ids = []
    altitudes = []
    velocities = []

    try:
        with open(log_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ids.append(int(row['packet_id']))
                altitudes.append(float(row['altitude']))
                velocities.append(float(row['velocity']))
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return

    if not ids:
        print("⚠️ No data found in log file.")
        return

    # Create plots
    plt.figure(figsize=(10, 8))

    # Altitude Plot
    plt.subplot(2, 1, 1)
    plt.plot(ids, altitudes, color='blue', label='Altitude')
    plt.title('Flight Telemetry Analysis')
    plt.ylabel('Altitude (m)')
    plt.grid(True)
    plt.legend()

    # Velocity Plot
    plt.subplot(2, 1, 2)
    plt.plot(ids, velocities, color='orange', label='Velocity')
    plt.xlabel('Packet ID')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)
    plt.legend()

    output_file = "flight_analysis.png"
    plt.savefig(output_file)
    print(f"✅ Analysis complete! Plot saved to: {output_file}")

if __name__ == "__main__":
    plot_flight_data()
