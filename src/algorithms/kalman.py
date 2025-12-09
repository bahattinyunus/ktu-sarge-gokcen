class KalmanFilter1D:
    """
    A simple 1D Kalman Filter implementation.
    Used for smoothing noisy sensor data (e.g., altitude).
    """
    def __init__(self, process_noise=0.1, measurement_noise=5.0, estimated_error=1.0, initial_value=0.0):
        self.q = process_noise       # Process noise covariance
        self.r = measurement_noise   # Measurement noise covariance
        self.p = estimated_error     # Estimation error covariance
        self.x = initial_value       # State estimate
        self.k = 0.0                 # Kalman gain

    def update(self, measurement):
        """
        Updates the filter with a new measurement and returns the filtered value.
        """
        # Prediction update (Simplified for 1D constant state model)
        self.p = self.p + self.q

        # Measurement update
        self.k = self.p / (self.p + self.r)
        self.x = self.x + self.k * (measurement - self.x)
        self.p = (1 - self.k) * self.p
        
        return self.x
