import socket
import json
import time

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"📡 Ground Station Receiver listening on {UDP_IP}:{UDP_PORT}")
    print("-" * 50)
    print(f"{'ID':<6} {'Alt(m)':<10} {'Vel(m/s)':<10} {'Status':<10}")
    print("-" * 50)

    # Open CSV file for logging
    with open("telemetry_log.csv", "w", encoding="utf-8") as log_file:
        log_file.write("packet_id,timestamp,altitude,velocity,status\n")

        try:
            while True:
                data, addr = sock.recvfrom(1024)
                try:
                    telemetry = json.loads(data.decode('utf-8'))
                    
                    # Print to console
                    print(f"{telemetry.get('packet_id', 0):<6} "
                          f"{telemetry.get('altitude', 0):<10.1f} "
                          f"{telemetry.get('velocity', 0):<10.1f} "
                          f"{telemetry.get('status', 'N/A'):<10}")
                    
                    # Write to CSV
                    log_file.write(f"{telemetry.get('packet_id')},{telemetry.get('timestamp')},"
                                   f"{telemetry.get('altitude')},{telemetry.get('velocity')},"
                                   f"{telemetry.get('status')}\n")
                    log_file.flush() # Ensure data is written immediately

                except json.JSONDecodeError:
                    print(f"⚠️ Received invalid data: {data}")

        except KeyboardInterrupt:
            print("\n🛑 Receiver stopped.")

if __name__ == "__main__":
    main()
