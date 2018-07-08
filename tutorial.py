from astropy.io import fits
import astropy.table as t
            
hdulist = fits.open('/media/celeste/Hypatia/MPL7/HYB/allmaps/manga-' + plate_num[i] + '-' + fiber_num[i] + '-MAPS-HYB10-GAU-MILESHC.fits.gz')
            
logcube = fits.open('/media/celeste/Hypatia/MPL7/LOGCUBES/manga-'+ str(plate_num[i])+ '-' + str(fiber_num[i]) + '-LOGCUBE.fits.gz')
            
drpall = t.Table.read('/home/celeste/Documents/astro_research/drpall-v2_3_1.fits')

fluxes = hdulist['EMLINE_GFLUX'].data
Ha = fluxes[18,:,:]

errs=(hdulist['EMLINE_GFLUX_IVAR'].data)**-0.5
Ha_err = errs[18,:,:]

OIII = fluxes[13,:,:]
o3_err = errs[13,:,:]

Hb = fluxes[11,:,:]
Hb_err = errs[11,:,:]

##assigns the plate id based on what is in the data cube
plate_id = hdulist['PRIMARY'].header['PLATEIFU']

##gets official plate number
plate_number = hdulist['PRIMARY'].header['PLATEID']
fiber_number = hdulist['PRIMARY'].header['IFUDSGN']

obj = drpall[drpall['plateifu']==plate_id][0]

contours_i = logcube['IIMG'].data

obj = drpall[drpall['plateifu']==plate_id][0]
Re = obj['nsa_elpetro_th50_r']
pa = obj['nsa_elpetro_phi']
