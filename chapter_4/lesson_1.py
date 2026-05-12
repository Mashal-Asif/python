import json
'''
import numpy as np
import matplotlib.pyplot as plt


#Lesson 1: Plotting with Matplotlib
#Example: Plotting sin(x) using matplotlib
def f(x):
    return np.sin(x)    
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = f(x)

plt.plot(x, y,label='f(x) = sin(x)',linestyle='-', color='blue',linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) = sin(x)')
plt.legend()
plt.grid(True)
plt.show()

#Lesson 2 Plotting Aircraft Telemetry using MatplotLib

with open('adsb_dataset.json', 'r') as f: # Open the telemetry data file
    data=json.load(f)['trace'] # Load the data from the file
    filtered_data=[]
    for aircraft in data: # Loop through each aircraft in the data
       if aircraft[8]!=None:
           filtered_data.append(aircraft) # Filter out aircraft with null altitude
           print(aircraft[0]) # Print the altitude of the aircraft
           
           # Display aircraft data
           aircraft=filtered_data[0][8]
           print(f"Flight {aircraft['flight']}: Airspeed is {aircraft['tas']} knots")
           print(aircraft)
           
airspeeds = []
for entry in filtered_data:
    if 'tas' in entry[8]:
        airspeeds.append(entry[8]['tas'])
print(airspeeds[:5])

plt.plot(airspeeds)
plt.xlabel('Data Point Index')
plt.ylabel('Airspeed (knots)')
plt.title('Aircraft Airspeed')
plt.grid(True)
plt.show()

#Excersise: 01

import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('spacecraft_thruster.csv','r')as f:
    data=csv.reader(f)
    next(data) # Skip the header row
    timestamps=[]
    thrust_value=[]
    for thruster in data:
        if thruster[2]!=None: # Check if the thrust value is not null   
           #timestamps.append(datetime.strptime(thruster[0], '%Y-%m-%d %H:%M:%S')) # Append timestamp to the list
           
           timestamps.append(
    datetime.strptime(thruster[0].split('.')[0], '%Y-%m-%d %H:%M:%S')
)
        thrust_value.append(float(thruster[2])) # Append thrust value to the list
plt.plot(timestamps, thrust_value)
plt.xlabel('Time')
plt.ylabel('Thrust Value')
plt.title('Spacecraft Thruster Data')
plt.grid(True)
plt.show()
'''
#Using Models and Fitting with Astropy

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

rng = np.random.default_rng(0)
x = np.linspace(-5., 5., 200)
y = 3 * np.exp(-0.5 * (x - 1.3)**2 / 0.8**2)
y += rng.normal(0., 0.2, x.shape)


g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
fit_g = fitting.LevMarLSQFitter()#this means we are using the Levenberg-Marquardt algorithm for fitting
g = fit_g(g_init, x, y)#fit the Gaussian model to the data


plt.figure(figsize=(8,5))
plt.plot(x, y, 'ko')
#plt.plot(x, t(x), label='Trapezoid')
from astropy.modeling import models

t_init = models.Trapezoid1D(amplitude=3., x_0=0., width=2., slope=1.)
fit_t = fitting.LevMarLSQFitter()
t = fit_t(t_init, x, y)

plt.plot(x, t(x), label='Trapezoid')
plt.plot(x, y, 'ko', label='Data')
plt.plot(x, g(x), label='Gaussian')
plt.xlabel('Position')
plt.ylabel('Flux')
plt.legend(loc=2)
plt.show()
#Excersise: 02
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling.models import BlackBody
from astropy import units as u
from astropy.visualization import quantity_support

black_body = BlackBody(temperature=3000*u.K)
wavelengths = np.arange(2000, 200000) * u.AA
flux = black_body(wavelengths)

with quantity_support():
    plt.figure()
    plt.semilogx(wavelengths, flux)
    plt.axvline(black_body.nu_max.to(u.AA, equivalencies=u.spectral()).value, ls='--')
    plt.show()