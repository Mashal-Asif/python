# Exercise:1 "Space Craft Telemetry modelling with numpy Arrays"
'''
import numpy as np
time_array = np.arange(0, 101, 1) #from 0, it will be inclusive, to 101, it will be exclusive, and step is 1
print(time_array.shape) #shape of the array

altitude_array=100*time_array #100m/s speed
# altitude(s)= velocity(m/s)*time(s)
print(altitude_array.shape) #printing the altitude array

acceleration = np.full_like(time_array, 9.81, dtype=float) #creating an array of the same shape as time_array, filled with the value 9.81, and specifying the data type as float
print(acceleration.shape) #printing the shape of the acceleration array 

velocity = np.sqrt (2*9.81*altitude_array) #calculating velocity using the formula v=sqrt(2*a*s)
print(velocity.shape) #printing the shape of the velocity array

# PRINT FULL ARRAYS 
print("Time:", time_array)
print("Altitude:", altitude_array)
print("Acceleration:", acceleration)
print("Velocity:", velocity)
'''
# Exercise:2 "Mission Profiling with numpy Arrays"
import numpy as np

# Generate simulated flight data
altitude = np.random.uniform(0, 10000, size=1000)  # Altitude in meters
velocity = np.random.uniform(0, 400, size=1000)  # Velocity in meters per second
acceleration = np.random.uniform(-20, 20, size=1000)  # Acceleration in meters per second squared

# Identify critical points
critical_altitude = altitude[altitude > 5000]
critical_velocity = velocity[velocity > 300]
critical_acceleration = acceleration[acceleration < -9.8]

# Concatenate critical point arrays
flight_profile = np.concatenate((critical_altitude, critical_velocity, critical_acceleration))

# Display the flight profile
print("Flight Profile:")
print(flight_profile)
mask = (altitude > 5000) & (velocity > 300) & (acceleration < -9.8)

flight_profile = np.column_stack((
    altitude[mask],
    velocity[mask],
    acceleration[mask]
))
print(flight_profile)