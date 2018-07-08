from astropy.io import fits
import astropy.table as t
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.image as img
import numpy as np

plate_num = ['7495']
fiber_num = ['12704']


for i in range(0, len(plate_num)):            
    hdulist = fits.open('/media/celeste/Hypatia/MPL7/HYB/allmaps/manga-' + plate_num[i] + '-' + fiber_num[i] + '-MAPS-HYB10-GAU-MILESHC.fits.gz')

    logcube = fits.open('/media/celeste/Hypatia/MPL7/LOGCUBES/manga-'+ plate_num[i]+ '-' + fiber_num[i] + '-LOGCUBE.fits.gz')

    drpall = t.Table.read('/home/celeste/Documents/astro_research/drpall-v2_3_1.fits')

    fluxes = hdulist['EMLINE_GFLUX'].data
    errs=(hdulist['EMLINE_GFLUX_IVAR'].data)**-0.5
    Ha = fluxes[18,:,:]
    Ha_err = errs[18,:,:]
    masks = hdulist['EMLINE_GFLUX_MASK'].data
    Ha_mask = masks[18,:,:]
    plate_id = hdulist['PRIMARY'].header['PLATEIFU']
    
    shape = (Ha.shape[1])
    shapemap = [-.25*shape, .25*shape, -.25*shape, .25*shape]
    '''
    #SIGNAL TO NOISE CUT
    badpix = (Ha/Ha_err) < 3
    Ha[badpix]=np.nan
    '''
    
    #MASK
    Ha[Ha_mask != 0] = np.nan
    
    fig = plt.figure(figsize=(30,18), facecolor='white')


    plt.title("H-alpha Flux")
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    plt.savefig('/home/celeste/Documents/astro_research/tutorial/' + str(plate_id) + '_ha_mask.png')
