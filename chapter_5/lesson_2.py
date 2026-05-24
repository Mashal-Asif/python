# Exercise 1: Create a sin(x) plot using Tkinter and Matplotlib
'''
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

window = tk.Tk() 
window.title('Sin Graph using Tkinter') 
# Setting the dimensions of the window to be 600px by 600px
window.geometry("600x600") 

def sin_function(x):
    return np.sin(x)

x = np.linspace(0, 2*np.pi, 100)  # Values from 0 to 2*pi
y = sin_function(x)
fig = Figure(figsize = (5, 5), 
                 dpi = 100) 

plot1 = fig.add_subplot(111)

# Plot the function
plot1.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x)')
# Add legend
plt.legend()


canvas = FigureCanvasTkAgg(fig, master = window)   
canvas.draw() 

# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack() 


toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

# Place the toolbar on the Tkinter window
canvas.get_tk_widget().pack()

window.mainloop()
'''

# Exercise 2: Create Tkinter plot of ODE of Object in Free Fall
g = -9.81  # Acceleration due to gravity (m/s^2)
t = np.linspace(0, 10, 1000)  # Time 
y0 = [0, 0] # initial condition

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

def free_fall_ode(y, t):
    return [y[1], g]

solution = odeint(free_fall_ode, y0, t)

# Extract position and velocity from the solution
y = solution[:, 0]  # position
v = solution[:, 1]  # velocity

window = tk.Tk() 
window.title('Object in Free Fall ODE') 
# Setting the dimensions of the window to be 600px by 600px
window.geometry("600x600")

fig = Figure(figsize = (8, 6), 
                 dpi = 100) 

# Add a subplot to the figure
plot1 = fig.add_subplot(111) 

plot1.plot(t, y, label='Vertical Position')
plt.xlabel('Time (s)')
plt.ylabel('Vertical Position (m)')
plt.title('Solution to Free-Fall ODE using odeint')
plt.legend()
plt.grid(True)

canvas = FigureCanvasTkAgg(fig, master = window)   
canvas.draw() 

# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack() 

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

# Place the toolbar on the Tkinter window
canvas.get_tk_widget().pack()

window.mainloop()


