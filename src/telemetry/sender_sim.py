import json
import random
import socket
import time
import os

def main():
    print("📡 Telemetry Simulator Started...")
    print("Sending data to UDP port 5005 (Localhost)")

    UDP_IP = os.getenv("TARGET_IP", "127.0.0.1")
    UDP_PORT = int(os.getenv("TARGET_PORT", 5005))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    start_time = time.time()
    
    # 3D Position State
    x, y, z = 0.0, 0.0, 0.0
    vx, vy, vz = 0.0, 0.0, 0.0

    print("🚀 Taking off...")

    # Simulation Loop
    for i in range(1000): 
        current_time = time.time() - start_time
        
        # Simple Physics Model
        if current_time < 5.0: # Burn phase (0-5s)
            az = 20.0 - 9.81
            ax = random.uniform(-0.5, 0.5) # Random wind buffeting
            ay = random.uniform(-0.5, 0.5)
            status = "ASCENT_BURN"
        elif vz > 0: # Coast phase
            az = -9.81 - (0.01 * vz**2) # Gravity + Drag
            ax = random.uniform(-0.2, 0.2)
            ay = random.uniform(-0.2, 0.2)
            status = "COASTING"
        else: # Descent phase
            az = -9.81 + (0.05 * vz**2) # Parachute drag
            ax = random.uniform(-2.0, 2.0) # High drift under parachute
            ay = random.uniform(-2.0, 2.0)
            status = "DESCENT"

        # Update Velocity (Integration)
        dt = 0.5
        vz += az * dt
        vx += ax * dt
        vy += ay * dt

        # Update Position (Integration)
        z += vz * dt
        x += vx * dt
        y += vy * dt

        # Ground collision
        if z < 0:
            z = 0
            status = "LANDED"

        packet = {
            "team_id": 12345,
            "packet_id": i,
            "timestamp": round(current_time, 2),
            "altitude": round(z, 2),
            "velocity": round(vz, 2),
            "pos_x": round(x, 2),
            "pos_y": round(y, 2),
            "status": status
        }
        
        message = json.dumps(packet).encode('utf-8')
        sock.sendto(message, (UDP_IP, UDP_PORT))
        print(f"Tx: {message}")
        
        if status == "LANDED":
            print("🛬 Rocket Landed.")
            break

        time.sleep(0.5)

    print("✅ Transmission Complete.")

if __name__ == "__main__":
    main()
