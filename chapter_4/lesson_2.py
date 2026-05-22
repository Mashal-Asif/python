# Exercise 1: Solving a simple ODE using Python
import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

def differential_equation(y, t):
    dydt = (y ** 2)  * t + (8 * t)
    return dydt

# initial condition 
y0 = 1
  
# values of time 
t = np.linspace(1,2) 
  
# Solving ODE 
y = odeint(differential_equation, y0, t) 


plt.plot(t,y) 
plt.xlabel("Time") 
plt.ylabel("Y") 
plt.title("Visualizing dy/dt ODE")
plt.show()

#Excersiese: 02
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
m = 1000  # Mass of the rocket (kg)
T = 20000  # Thrust of the rocket (N)

def rocket_motion_ode(t, state):    
    # Extract state variable (horizontal velocity)
    v = state[0]
    D = 500*t  # Drag force as a function of time (N)
    # Compute acceleration (Newton's second law)
    a = (T - D) / m

    return [a]

v0 = 0  # Initial horizontal velocity (m/s)
state0 = [v0]
# Time span
t_span = (0, 100)

sol = solve_ivp(rocket_motion_ode, t_span, state0, t_eval=np.linspace(t_span[0], t_span[1], 1000))

plt.plot(sol.t, sol.y[0])
plt.xlabel('Time (s)')
plt.ylabel('Horizontal Velocity (m/s)')
plt.title('Rocket Horizontal Motion')
plt.grid(True)
plt.show()