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
    
    velocity = hdulist['EMLINE_GVEL'].data[18,...]
    velocity_err = (hdulist['EMLINE_GVEL_IVAR'].data[18,...])**-0.5
    
    Ha = fluxes[18,:,:]
    Hb = fluxes[11,:,:]
    O3 = fluxes[13,:,:]
    N2 = fluxes[19,:,:]
    s21 = fluxes[20,:,:]
    
    Ha_err = errs[18,:,:]
    Hb_err = errs[11,:,:]
    O3_err = errs[13,:,:]
    N2_err = errs[19,:,:]
    s21_err = errs[20,:,:]
    
    masks = hdulist['EMLINE_GFLUX_MASK'].data
    Ha_mask = masks[18,:,:]
    Hb_mask = masks[11,:,:]
    O3_mask = masks[13,:,:]
    N2_mask = masks[19,:,:]
    s21_mask = masks[20,:,:]
    vel_mask = hdulist['EMLINE_GFLUX_MASK'].data[18,...]
    
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
    Hb[Hb_mask != 0] = np.nan
    O3[O3_mask != 0] = np.nan
    N2[N2_mask != 0] = np.nan
    s21[s21_mask != 0] = np.nan
    velocity[vel_mask != 0] = np.nan
    
    #badpix = (velocity/velocity_err) < 3
    #velocity[badpix] = np.nan
    
    fig = plt.figure(figsize=(30,18), facecolor='white')
    
    #HA SUBPLOT
    
    ha_plot = fig.add_subplot(2, 3, 4)
    plt.title(r'H$\alpha$ Flux Map')
    ha_plot.imshow(Ha, cmap = "viridis", extent = shapemap, zorder = 1)
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    #HB SUBPLOT
    
    hb_plot = fig.add_subplot(2, 3, 3)
    plt.title(r'H$\beta$ Flux Map')
    hb_plot.imshow(Hb, cmap = "gist_earth", extent = shapemap, zorder = 1)
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    #O3 SUBPLOT
    o3_plot = fig.add_subplot(2, 3, 1)
    plt.title('OIII Flux Map')
    o3_plot.imshow(O3, cmap = "gist_ncar", extent = shapemap, zorder = 1)
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    #N2 SUBPLOT
    n2_plot = fig.add_subplot(2, 3, 2)
    plt.title('NII Flux Map')
    n2_plot.imshow(N2, cmap = "magma", extent = shapemap, zorder = 1)
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    #S21 SUBPLOT
    s21_plot = fig.add_subplot(2, 3, 5)
    plt.title('S21 Flux Map')
    s21_plot.imshow(s21, cmap = "jet", extent = shapemap, zorder = 1)
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    #VELOCITY SUBPLOT
    vel_plot = fig.add_subplot(2, 3, 6)
    plt.title(r'H$\alpha$ Gas Velocity')
    plt.imshow(velocity, cmap = "rainbow", extent = shapemap, zorder = 1)
    
    cb_vel = plt.colorbar(shrink = .7)
    cb_vel.set_label('km/s', rotation = 270, labelpad = 25)
    
    plt.xlabel('Arcseconds')
    plt.ylabel('Arcseconds')
    
    
    #plt.show()

    plt.savefig('/home/celeste/Documents/astro_research/tutorial/' + str(plate_id) + '_full_six_fig_cb.png')
    
