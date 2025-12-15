@echo off
echo 🚀 Starting Teknofest Rocket System...

echo 1. Launching Ground Station Receiver...
start "Ground Station" cmd /k "python src/telemetry/receiver_sim.py"

echo 2. Launching Mission Control Dashboard...
start "Mission Control" cmd /k "streamlit run src/dashboard/dashboard.py"

echo 3. Launching Flight Computer Simulator...
timeout /t 3
start "Flight Computer" cmd /k "python src/telemetry/sender_sim.py"

echo ✅ All systems operational! Use the Dashboard to control the rocket.
pause
