# 💻 Source Code Documentation

This directory contains the simulation and telemetry software for the rocket.

## 📂 Structure

- **`simulation/`**: Contains flight dynamics simulations.
    - `rocket_flight.py`: A 1D vertical flight simulator.
- **`telemetry/`**: Contains ground station and transceiver simulations.
    - `sender_sim.py`: Simulates sending telemetry packets via UDP.

## 🚀 How to Run

### Requirements
Ensure you have the dependencies installed:
```bash
pip install -r ../requirements.txt
```

### Running the Flight Simulation
```bash
python simulation/rocket_flight.py
```
This will run the physics simulation and print the apogee results.

### Running the Telemetry Simulator
```bash
python telemetry/sender_sim.py
```
This will start sending dummy JSON packets to localhost UDP port 5005.
