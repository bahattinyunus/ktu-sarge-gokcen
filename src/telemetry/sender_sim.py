import json
import random
import socket
import time
import os
import threading

# Uplink Config
CMD_PORT = int(os.getenv("ROCKET_CMD_PORT", 5006))

# Simulation State
current_status = "IDLE"
mission_start_time = 0
reset_flag = False

def command_listener():
    """Listens for UDP commands on a separate thread."""
    global current_status, mission_start_time, reset_flag
    
    cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cmd_sock.bind(("0.0.0.0", CMD_PORT))
    print(f"👂 Listening for commands on port {CMD_PORT}...")

    while True:
        data, addr = cmd_sock.recvfrom(1024)
        cmd = data.decode('utf-8').strip().upper()
        print(f"📩 Command Received: {cmd}")

        if cmd == "ARM":
            current_status = "READY"
        elif cmd == "LAUNCH":
            if current_status == "READY":
                current_status = "ASCENT_BURN"
                mission_start_time = time.time()
        elif cmd == "DEPLOY_CHUTE":
            current_status = "DESCENT"
        elif cmd == "RESET":
            current_status = "IDLE"
            reset_flag = True

def main():
    global current_status, mission_start_time, reset_flag
    
    print("📡 Telemetry Simulator Started...")
    
    # Start Listener
    t = threading.Thread(target=command_listener, daemon=True)
    t.start()

    UDP_IP = os.getenv("TARGET_IP", "127.0.0.1")
    UDP_PORT = int(os.getenv("TARGET_PORT", 5005))
    
    # Tuz Golu Launch Site
    LAUNCH_LAT = 38.8200
    LAUNCH_LON = 33.3300

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Physics State
    x, y, z = 0.0, 0.0, 0.0
    vx, vy, vz = 0.0, 0.0, 0.0

    print("⏳ Waiting for commands...")

    while True:
        if reset_flag:
            x, y, z = 0.0, 0.0, 0.0
            vx, vy, vz = 0.0, 0.0, 0.0
            reset_flag = False
            print("🔄 Simulation Reset.")

        # Time Management
        if current_status in ["IDLE", "READY"]:
            # Just send heartbeat
            dt = 0.5
        else:
            dt = 0.5
            mission_time = time.time() - mission_start_time
            
            # Physics Calculation based on State
            if current_status == "ASCENT_BURN":
                az = 25.0 - 9.81
                if mission_time > 5.0:
                    current_status = "COASTING"
            elif current_status == "COASTING":
                az = -9.81 - (0.01 * vz**2)
                if vz < 0:
                     # Auto-deploy at apogee (normally), but let's wait for gravity or command
                     pass
            elif current_status == "DESCENT":
                 az = -9.81 + (0.05 * vz**2)
                 if vz > -5: az = -9.81 # Terminal velocity clamp roughly

            if current_status in ["ASCENT_BURN", "COASTING", "DESCENT"]:
                # Integration
                vz += az * dt
                z += vz * dt
                
                # Drift
                x += random.uniform(-1, 1)
                y += random.uniform(-1, 1)

            # Ground Check
            if z < 0:
                z = 0
                if current_status not in ["IDLE", "READY"]:
                    current_status = "LANDED"

        # Coordinates
        lat = LAUNCH_LAT + (y / 111000.0)
        lon = LAUNCH_LON + (x / (111000.0 * 0.78))

        # Packet Generation
        packet = {
            "team_id": 12345,
            "packet_id": 0, # Simplified
            "timestamp": time.time(),
            "altitude": round(z, 2),
            "velocity": round(vz, 2),
            "pos_x": round(x, 2),
            "pos_y": round(y, 2),
            "gps_lat": lat,
            "gps_long": lon,
            "status": current_status
        }
        
        msg = json.dumps(packet).encode('utf-8')
        sock.sendto(msg, (UDP_IP, UDP_PORT))
        print(f"Tx ({current_status}): {msg[:50]}...")
        
        time.sleep(dt)

if __name__ == "__main__":
    main()
