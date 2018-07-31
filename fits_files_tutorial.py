import astropy.table as t
from astropy.io import fits
import numpy as np
import math
from astropy.table import Table, Column

#My specified galaxy IDs. You can type them in separately, read them from another fits file, or another text file, etc. These are just for demonstration purposes
galaxyIDs = ['10001-3703', '10001-9101', '7443-12702', '7443-1901', '8134-6103']

#Reading from another fits file. You should already know how to do thi
drpall = t.Table.read('/home/celeste/Documents/astro_research/drpall-v2_3_1.fits')

#Creates the empty arrays
inclination = []
gal_mass = []

#Creates an array of each value I want to associate with an ID
for x in range(0, len(galaxyIDs)):
    obj = drpall[drpall['plateifu']==str(galaxyIDs[x])][0]
    ba = obj['nsa_elpetro_ba']
    mass = math.log10(obj['nsa_elpetro_mass'])-np.log10(.49)
    inclination.append(ba)
    gal_mass.append(mass)
    
    
gal_mass = np.asarray(gal_mass)
inclination = np.asarray(inclination)
galaxyIDs = np.asarray(galaxyIDs)

t = Table()

t['GAL_ID'] = Column(galaxyIDs, description = 'Plate IFU' )
t['MASS'] = Column(gal_mass, description = 'Mass of the galaxy' )
t['PA'] = Column(inclination, description = 'b/a')

t.write('/home/celeste/Documents/astro_research/tutorial/tutorialfilev1.fits')
