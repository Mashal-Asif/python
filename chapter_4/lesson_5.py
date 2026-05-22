# Exercise 1: Simulating 2D Orbital Mechanics for Earth

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def orbit_equations_de(state_vectors, t, G, M):
    # y[0] and y[1] represent the x and y positions respectively
    # y[2] and y[3] represent the x and y velocities respectively
    dxdt = state_vectors[2]
    dydt = state_vectors[3]
    dvxdt = -G * M * state_vectors[0] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    dvydt = -G * M * state_vectors[1] / (np.sqrt(state_vectors[0]**2 + state_vectors[1]**2))**3
    return [dxdt, dydt, dvxdt, dvydt]

altitude = 400e3
initial_velocity = 7800

# Define initial conditions
y0 = [0.0, altitude, initial_velocity, 0.0]  # Initial position at (1, 0) and velocity (0, 1)

# Define time points for integration
t = np.linspace(0, 10, 1000)

# Define constants
G = 6.67430e-11  # Gravitational constant
M = 5.972e24  # Mass of Earth

# Perform numerical integration
solution = odeint(orbit_equations_de, y0, t, args=(G, M))

# Plot the orbit trajectory
plt.figure(figsize=(8, 8))
plt.plot(solution[:, 0], solution[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Orbit Simulation of Earth')
plt.grid(True)
plt.axis('equal')
plt.show()