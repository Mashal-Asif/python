# Matplotlib
import matplotlib.pyplot as plt
# Exercise: 01 "Supernova Brightness"
# Sample dataset (time points and brightness measurements)
time_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Time points
brightness = [10, 30, 80, 140, 120, 100, 80, 60, 30, 10]  # Brightness measurements

plt.plot(time_points, brightness, color='purple', linestyle='--', marker='o', markersize=5)
plt.xlabel('Time (days)')
plt.ylabel('Brightness (arbitrary units)')
plt.title('Brightness of Supernova')

# Show plot
plt.show()

# Excercise: 02 
import math
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*math.pi, 100)
y = np.tan(x)

plt.plot(x, y)
plt.title('Plot of tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

x = np.linspace(0, 2*math.pi, 50)
y = np.tan(x)

plt.plot(x, y)
plt.title('Plot of tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

x = np.linspace(0, 2*math.pi, 50)
y1 = np.tan(x)
y2 = np.cos(x)

plt.plot(x, y1, label='tan(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of tan(x) and cos(x)')
plt.grid(True)
plt.show()