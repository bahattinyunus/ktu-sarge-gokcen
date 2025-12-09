import time

import matplotlib.pyplot as plt
import numpy as np


def simulate_flight(burn_time=5.0, avg_thrust=1500, wet_mass=20.0, dry_mass=10.0):
    """
    Simulates a 1D vertical rocket flight.

    Args:
        burn_time (float): Motor burn duration in seconds.
        avg_thrust (float): Average thrust in Newtons.
        wet_mass (float): Launch mass in kg.
        dry_mass (float): Mass after burnout in kg.
    """
    dt = 0.05  # Time step
    g = 9.81  # Gravity

    # Time array
    t_max = 30.0
    times = np.arange(0, t_max, dt)

    # State arrays
    altitude = np.zeros_like(times)
    velocity = np.zeros_like(times)
    acceleration = np.zeros_like(times)
    mass = np.ones_like(times) * dry_mass

    print(f"🚀 Simulation Started: Wet Mass={wet_mass}kg, Thrust={avg_thrust}N")

    # Flight Loop
    for i, t in enumerate(times[:-1]):
        # 1. Update Mass (Linear burn)
        if t < burn_time:
            mass[i] = wet_mass - ((wet_mass - dry_mass) / burn_time) * t
            thrust = avg_thrust
        else:
            mass[i] = dry_mass
            thrust = 0.0

        # 2. Forces
        # Drag approximation: Fd = 0.5 * rho * Cd * A * v^2
        # Using a simplified drag coefficient k
        k = 0.05
        drag = k * velocity[i] ** 2 * np.sign(velocity[i])

        weight = mass[i] * g
        net_force = thrust - weight - drag

        # 3. Kinematics
        acc = net_force / mass[i]
        acceleration[i] = acc

        velocity[i + 1] = velocity[i] + acc * dt
        altitude[i + 1] = altitude[i] + velocity[i] * dt

        # Stop if ground hit
        if altitude[i + 1] < 0:
            altitude[i + 1 :] = 0
            velocity[i + 1 :] = 0
            break

    apogee = np.max(altitude)
    print(f"✨ Flight Complete! Apogee: {apogee:.2f} meters")

    return times, altitude, velocity, acceleration


if __name__ == "__main__":
    t, h, v, a = simulate_flight()

    # Plotting
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(t, h, label="Altitude (m)", color="blue")
        plt.plot(t, v, label="Velocity (m/s)", color="orange")
        plt.axhline(
            y=np.max(h), color="red", linestyle="--", label=f"Apogee: {np.max(h):.1f}m"
        )
        plt.title("Teknofest 2026 - Flight Simulation")
        plt.xlabel("Time (s)")
        plt.legend()
        plt.grid(True)
        # plt.show() # Commented out for headless environments
        print("📈 Graph generated (display skipped).")
    except Exception as e:
        print(f"Warning: Could not plot ({e})")
