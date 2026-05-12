from astropy.io import fits

with fits.open('M13.fits') as hdul:
    hdul.info()
    print(hdul[0].header)
    
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
plt.style.use(astropy_mpl_style)

image_file = get_pkg_data_filename('./M13.fits')
image_data = fits.getdata(image_file, ext=0)

print(image_data.shape)

plt.figure()
plt.imshow(image_data)
plt.colorbar()

# Excersise 1: Open the FITS file and print the header information.
from astropy.io import fits
import matplotlib.pyplot as plt

# Open FITS file safely
with fits.open('M6707HH.fits') as hdul:

    # 1. Print HDU info
    hdul.info()

    # 2. Print header of Primary HDU
    header = hdul[0].header
    print(header)

    # 3. Print image dimensions
    image_data = hdul[0].data
    print("Image shape:", image_data.shape)

    # 4. Visualize FITS image
    plt.figure(figsize=(8, 6))
    plt.imshow(image_data, cmap='plasma', origin='lower')
    plt.colorbar(label='Intensity')
    plt.title("FITS Image Visualization")
    plt.show()
