#Excersise: 01

import matplotlib.pyplot as plt
from photutils.datasets import make_4gaussians_image
from photutils.aperture import CircularAperture, ApertureStats

data = make_4gaussians_image()

# Create circular aperture
aperature = CircularAperture((150, 25), 8)

# Obtain aperture statistics
statistics = ApertureStats(data, aperature)

plt.figure(figsize=(8, 8))
plt.imshow(data, cmap='gray')
aperature.plot(color='blue', lw=1.5)
plt.colorbar(label='Counts')
plt.title('Circular Aperture Image')
plt.show()

print("Centroid:", statistics.centroid)
print("Bounding Box:", statistics.bbox)
print("Sum:", statistics.sum)
print("Standard Deviation:", statistics.std)
print("Number of Aperatures:", statistics.n_apertures)
print("Median:", statistics.median)
print("Eccentricity:", statistics.eccentricity)

#Excersise: 02

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models
from astropy import units as u
from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum

np.random.seed(0)
x = np.linspace(0., 10., 200)
y = 3 * np.exp(-0.5 * (x- 6.3)**2 / 0.8**2)
y += np.random.normal(0., 0.2, x.shape)

spectra = Spectrum1D(flux=y*u.Jy, spectral_axis=x*u.um)
continuum_fit = fit_generic_continuum(spectra)
y_continuum_fit = continuum_fit(x*u.um)

f, ax = plt.subplots()  
ax.plot(x, y)  
ax.plot(x, y_continuum_fit)  
ax.set_title("Continuum Fitting")  
ax.grid(True)
plt.show()