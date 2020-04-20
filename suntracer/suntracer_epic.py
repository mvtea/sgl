'''
FILE: suntracer.py
AUTHOR: Mason Tea
PURPOSE: Raytrace gravitational lensing by a point mass.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

import aux
from PIL import Image
from astropy.io import fits
from astropy.visualization import astropy_mpl_style
#plt.style.use(astropy_mpl_style)

### CONVERT PNG TO FITS (one-time use)

'''
png = Image.open('EPIC_smol.png')
rgb_im = png.convert('RGB')
rgb_im.save('EPIC_smol_rgb.jpg')


image = Image.open('EPIC_smol_rgb.jpg')
xsize,ysize = image.size

r,g,b = image.split()
r_data = np.array(r.getdata())
g_data = np.array(g.getdata())
b_data = np.array(b.getdata())

r_data = r_data.reshape(ysize,xsize)
g_data = g_data.reshape(ysize,xsize)
b_data = b_data.reshape(ysize,xsize)

red = fits.PrimaryHDU(data=r_data)
red.header['LATOBS'] = "32:11:56" # add spurious header info
red.header['LONGOBS'] = "110:56"
red.writeto('EPIC_smol_red.fits')

green = fits.PrimaryHDU(data=g_data)
green.header['LATOBS'] = "32:11:56"
green.header['LONGOBS'] = "110:56"
green.writeto('EPIC_smol_green.fits')

blue = fits.PrimaryHDU(data=b_data)
blue.header['LATOBS'] = "32:11:56"
blue.header['LONGOBS'] = "110:56"
blue.writeto('EPIC_smol_blue.fits')
'''

### DEFINITIONS ###

nx = 2048                                                            # Pixels in image plane
ny = 2048                                                             # Pixels in source plane

xl = 100.0                                                            # Size of image plane covered (theta_E)
yl = 17500.0                                                            # Size of source plane covered (theta_E)

### LENS PARAMETERS ###

xlens = 0.0                                                         # Lens x-position
ylens = 0.0                                                         # Lens y-position
mlens = 2000000.0                                                         # Lens mass

xs = 2.0 * xl / (nx - 1)                                            # Pixel size on image map
ys = 2.0 * yl / (ny - 1)                                            # Pixel size on source map

### SOURCE PARAMETERS ###

xpos = 0.0                                                          # Source x-position
ypos = 0.0                                                          # Source y-position
rad = 1.0                                                           # Source size

# Convert to pixels

ipos = int(round(xpos / ys))
jpos = int(round(-ypos / ys))
rpix = rad / ys

#src = aux.cgs(ny,rpix,jpos,ipos)                                      # Source plane)
src_r = aux.fitsim('images/fits/EPIC_red.fits')
src_g = aux.fitsim('images/fits/EPIC_green.fits')
src_b = aux.fitsim('images/fits/EPIC_blue.fits')

img_r = np.zeros((nx,nx))                                               # Image plane
img_g = np.zeros((nx,nx))                                               # Image plane
img_b= np.zeros((nx,nx))                                               # Image plane

### RAYTRACER ###

j1, j2 = np.mgrid[0:nx,0:nx]
x1 = -xl + j2 * xs
x2 = -xl + j1 * xs

y1, y2 = aux.pt_lens(x1, x2, xlens+0.1, ylens, mlens)
i2 = np.round((y1 + yl) / ys)
i1 = np.round((y2 + yl) / ys)

ind = (i1 >= 0) & (i1 < ny) & (i2 >= 0) & (i2 < ny)

i1n = i1[ind]
i2n = i2[ind]
j1n = j1[ind]
j2n = j2[ind]

for i in np.arange(np.size(i1n)):
    img_r[int(j1n[i]),int(j2n[i])] = src_r[int(i1n[i]),int(i2n[i])]
    img_g[int(j1n[i]),int(j2n[i])] = src_g[int(i1n[i]),int(i2n[i])]
    img_b[int(j1n[i]),int(j2n[i])] = src_b[int(i1n[i]),int(i2n[i])]

### PLOT ###


fig = plt.figure(1)
ax = plt.subplot(121)
reds = ax.imshow(src_g, extent = (-yl,yl,-yl,yl), cmap='bone')
#greens = ax.imshow(src_g, extent = (-yl,yl,-yl,yl), cmap='Greens')
#blues = ax.imshow(src_b, extent = (-yl,yl,-yl,yl), cmap='Blues')
plt.axis('off')
fa = np.sum(src_g)
ax.set_title('Flux = ' + str(fa))


ax = plt.subplot(122)
plt.imshow(img_g, extent = (-xl,xl,-xl,xl), cmap='bone')
#ax.imshow(img_g, extent = (-xl,xl,-xl,xl), cmap='Greens')
#ax.imshow(img_b, extent = (-xl,xl,-xl,xl), cmap='Blues')
plt.axis('off')
fb = np.sum(img_g)*(xs**2/ys**2)
ax.set_title('Flux = ' + str(fb))

plt.show()
