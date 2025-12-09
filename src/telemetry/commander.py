import socket
import os

# Uplink Configuration (Ground -> Rocket)
ROCKET_IP = os.getenv("ROCKET_IP", "127.0.0.1")
ROCKET_CMD_PORT = int(os.getenv("ROCKET_CMD_PORT", 5006))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command_str):
    """Sends a text command to the rocket simulation."""
    try:
        msg = command_str.encode('utf-8')
        sock.sendto(msg, (ROCKET_IP, ROCKET_CMD_PORT))
        print(f"📡 Uplink Sent: {command_str}")
        return True
    except Exception as e:
        print(f"❌ Uplink Error: {e}")
        return False

# Convenience functions for dashboard
def arm_rocket(): send_command("ARM")
def launch_rocket(): send_command("LAUNCH")
def deploy_chute(): send_command("DEPLOY_CHUTE")
def reset_simulation(): send_command("RESET")
