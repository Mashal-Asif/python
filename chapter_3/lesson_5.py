from astroquery.esa.jwst import Jwst
import astropy.units as u
from astropy.coordinates import SkyCoord

print(Jwst.get_status_messages())

import astropy.units as u
coord = SkyCoord(ra=53, dec=-27, unit=(u.degree, u.degree), frame='icrs')
width = u.Quantity(5, u.deg)
height = u.Quantity(5, u.deg)
result = Jwst.query_region(coordinate=coord, width=width, height=height)
print(result)