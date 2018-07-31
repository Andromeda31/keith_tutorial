from astropy.io import fits
import numpy as np
from astropy.table import Table, Column

files = fits.open('/home/celeste/Documents/astro_research/tutorial/tutorialfilev1.fits')

#print(files[1].header)

ids = files[1].data['GAL_ID']
mass = files[1].data['MASS']
pa = files[1].data['PA']

print(ids)
print(mass)
print(pa)
