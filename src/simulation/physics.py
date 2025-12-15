import random

class RocketPhysics:
    def __init__(self, initial_x=0, initial_y=0, initial_z=0):
        self.x = initial_x
        self.y = initial_y
        self.z = initial_z
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.az = 0.0
        
        self.g = 9.81
    
    def update(self, dt, status):
        """
        Updates the rocket state based on the current status and time step.
        """
        
        # Determine acceleration based on status
        if status == "ASCENT_BURN":
            # Thrust > Gravity
            self.az = 25.0 - self.g 
        elif status == "COASTING":
            # Drag + Gravity
            # Simple drag model: Fd ~ v^2
            drag_factor = 0.01
            drag = drag_factor * (self.vz ** 2)
            self.az = -self.g - (drag * (1 if self.vz > 0 else -1))
            
        elif status == "DESCENT":
            # Parachute drag (Terminal velocity approx 5-10 m/s)
            target_descent_vel = -8.0 # m/s
            
            # Simple P-control to reach terminal velocity
            error = target_descent_vel - self.vz
            self.az = error * 2.0 # gain
            
            # Clamp acceleration strictly if needed, but F=ma usually handles it
            
        elif status in ["IDLE", "READY", "LANDED"]:
            self.az = 0
            self.vz = 0
            if status == "LANDED":
                self.z = 0
                
        # Integration (Euler)
        self.vz += self.az * dt
        self.z += self.vz * dt
        
        # Lateral Drift (Random wind)
        if status in ["ASCENT_BURN", "COASTING", "DESCENT"]:
            self.vx += random.uniform(-0.1, 0.1)
            self.vy += random.uniform(-0.1, 0.1)
            
            # Dampen lateral velocity slightly
            self.vx *= 0.99
            self.vy *= 0.99
            
            self.x += self.vx * dt
            self.y += self.vy * dt
            
        # Ground collision
        if self.z < 0:
            self.z = 0
            self.vz = 0
            self.vx = 0
            self.vy = 0
            
        return {
            "x": self.x, "y": self.y, "z": self.z,
            "vx": self.vx, "vy": self.vy, "vz": self.vz,
            "az": self.az
        }
