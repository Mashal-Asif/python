# Exercise 1: Visualizing the Spectra of Ganymede

import glob

from astropy.io import fits
from specutils import Spectrum
from astropy.visualization import quantity_support
from astropy import units as u
import matplotlib.pyplot as plt
import numpy as np

file = fits.open('ganymede.fits')

file.info()

header = file[0].header
data = file[0].data

print(header[:5])

# Create wavelength axis manually
wavelength = np.arange(len(data)) * u.AA

# Create Spectrum object
spectra = Spectrum(
    flux=data * u.dimensionless_unscaled,
    spectral_axis=wavelength
)

quantity_support()

fig, ax = plt.subplots()

plt.title("1D Spectra Visualization of Ganymede")

ax.step(spectra.spectral_axis, spectra.flux)

plt.xlabel("Wavelength")
plt.ylabel("Relative Flux")

plt.show()

#Exercise 2: Generate a False Color Composite

import numpy as np
from glob import glob
import rasterio as rio
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

np.seterr(divide='ignore', invalid='ignore')
bands = glob("satellite-bands/*B?*.tiff")
bands.sort()

if not bands:
    raise FileNotFoundError(
        "No satellite-band TIFF files found in 'satellite-bands/'. "
        "Check that the data are located in chapter_4/satellite-bands and try again."
    )

data = []
for band in bands:
    with rio.open(band, 'r') as file:
        data.append(file.read(1))
stack_data = np.stack(data)

rgb = ep.plot_rgb(stack_data, 
                  rgb=(4, 3, 2), 
                  figsize=(10, 16))
plt.show()
 