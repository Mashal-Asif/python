import spiceypy as spice

import numpy as np
import matplotlib.pyplot as plt 


# Print out the toolkit version
spice.tkvrsn("TOOLKIT")

spice.furnsh("./kernels/cassMetaK.txt")


step = 4000
# Specify dates
utc = ['Jun 20, 2004', 'Dec 1, 2005']

etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print("Ephemeris Time One: {}, Ephemeris Time Two: {}".format(etOne, etTwo))


# Calculate time range
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]

print(times[0:3])


# Running spkpos
positions, lightTimes = spice.spkpos('Cassini', times, 'J2000', 'NONE', 'SATURN BARYCENTER')

# Print out Positioning (X, Y, Z)
print("Positions: ", positions[0])

# Print out Light Times
print("Light Times: ", lightTimes[0])


spice.kclear()

positions = np.asarray(positions).T # positions is a list, make it an ndarray for easier indexing
fig = plt.figure(figsize=(9, 9))
ax  = fig.add_subplot(111, projection='3d')
ax.plot(positions[0], positions[1], positions[2])
plt.title('Cassini Positioning Visualization made with SpiceyPy')
plt.show()