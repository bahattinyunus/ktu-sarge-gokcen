import json
import random
import socket
import time


def generate_packet(packet_id):
    """Generates a dummy telemetry packet."""
    return {
        "team_id": 12345,
        "packet_id": packet_id,
        "timestamp": time.time(),
        "pressure": 101325 - (packet_id * 10) + random.uniform(-5, 5),
        "altitude": packet_id * 5.5 + random.uniform(-0.5, 0.5),
        "velocity": packet_id * 1.2,
        "gps_lat": 41.0 + (packet_id * 0.0001),
        "gps_long": 29.0 + (packet_id * 0.0001),
        "status": "ASCENT" if packet_id < 100 else "DESCENT",
    }


def main():
    print("📡 Telemetry Simulator Started...")
    print("Sending data to UDP port 5005 (Localhost)")

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet_count = 0
    try:
        while packet_count < 20:  # Send 20 packets then stop for demo
            data = generate_packet(packet_count)
            message = json.dumps(data).encode("utf-8")

            sock.sendto(message, (UDP_IP, UDP_PORT))
            print(f"Tx: {message}")

            time.sleep(0.5)
            packet_count += 1

        print("✅ Transmission Complete.")

    except KeyboardInterrupt:
        print("Interrupted.")


if __name__ == "__main__":
    main()
