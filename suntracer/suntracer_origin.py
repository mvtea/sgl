'''
FILE: suntracer.py
AUTHOR: Mason Tea
PURPOSE: Raytrace gravitational lensing by a point mass.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

import aux

import PIL as pil

### DEFINITIONS ###

nx = 1000                                                            # Pixels in image plane
ny = 1000                                                             # Pixels in source plane

xl = 100.0                                                            # Size of image plane covered (theta_E)
yl = 100.0                                                            # Size of source plane covered (theta_E)

### LENS PARAMETERS ###

xlens = 0.0                                                         # Lens x-position
ylens = 0.0                                                         # Lens y-position
mlens = 1.0                                                         # Lens mass

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

src = aux.cgs(ny,rpix,jpos,ipos)                                      # Source plane
b = np.zeros((nx,nx))                                               # Image plane

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
    b[int(j1n[i]),int(j2n[i])] = src[int(i1n[i]),int(i2n[i])]

### PLOT ###

fig = plt.figure(1)
ax = plt.subplot(121)
ax.imshow(src, extent = (-yl,yl,-yl,yl),cmap='hot')
fa = np.sum(src)
ax.set_title('Flux = ' + str(np.round(fa,2)))
plt.axis('off')

ax = plt.subplot(122)
ax.imshow(b, extent = (-xl,xl,-xl,xl),cmap='hot')
fb = np.sum(b)*(xs**2/ys**2)
ax.set_title('Flux = ' + str(np.round(fb,2)))
plt.axis('off')


plt.show()
