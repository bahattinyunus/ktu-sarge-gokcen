import json
import random
import socket
import time
import os
import threading
import sys

# Ensure we can import from src (if running as script)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

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
    
    # Physics Engine
    from src.simulation.physics import RocketPhysics
    physics = RocketPhysics()

    print("⏳ Waiting for commands...")

    while True:
        if reset_flag:
            physics = RocketPhysics() # Reset state
            reset_flag = False
            print("🔄 Simulation Reset.")

        # Time Management
        if current_status in ["IDLE", "READY"]:
            # Just send heartbeat
            dt = 0.5
            state = physics.update(dt, current_status) # Updates timestamps/idle state
        else:
            dt = 0.5
            mission_time = time.time() - mission_start_time
            
            # Flight Logic (State Transitions)
            if current_status == "ASCENT_BURN":
                if mission_time > 5.0:
                    current_status = "COASTING"
            elif current_status == "COASTING":
                if physics.vz < 0 and physics.z > 0:
                    # Automatic apogee detection (optional, or wait for command)
                    # For now just let it fall until logic or command changes it
                    pass
            elif current_status == "DESCENT":
                pass

            # Update Physics
            state = physics.update(dt, current_status)

            # Ground Check for Auto-Landing
            if state["z"] <= 0 and current_status == "DESCENT":
                 current_status = "LANDED"
                 
        x, y, z = state["x"], state["y"], state["z"]
        vz = state["vz"]

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
