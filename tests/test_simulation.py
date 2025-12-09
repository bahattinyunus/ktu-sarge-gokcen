import os
import sys
import unittest

# Add the src directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from simulation.rocket_flight import simulate_flight


class TestRocketSimulation(unittest.TestCase):
    def test_simulation_returns_data(self):
        """Test that the simulation returns arrays of data."""
        t, h, v, a = simulate_flight(burn_time=5.0, avg_thrust=1500)

        self.assertTrue(len(t) > 0)
        self.assertTrue(len(h) > 0)
        self.assertEqual(len(t), len(h))
        self.assertEqual(len(h), len(v))

    def test_apogee_positive(self):
        """Test that the rocket goes up (positive altitude)."""
        t, h, v, a = simulate_flight(burn_time=5.0, avg_thrust=2000)
        apogee = max(h)
        self.assertGreater(
            apogee, 0, "Apogee should be positive with sufficient thrust"
        )

    def test_impact(self):
        """Test that the rocket eventually hits the ground (altitude returns to 0)."""
        # Use weak thrust and short burn to ensure it lands within 30s
        t, h, v, a = simulate_flight(
            burn_time=2.0, avg_thrust=500, wet_mass=20.0, dry_mass=15.0
        )
        # The last altitude point should be 0
        self.assertEqual(h[-1], 0)


if __name__ == "__main__":
    unittest.main()
