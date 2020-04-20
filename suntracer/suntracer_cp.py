'''
FILE: suntracer_cp.py
AUTHOR: Mason Tea
PURPOSE: Raytrace gravitational lensing by a point mass.
'''

### LIBRARIES ###

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

import aux

### DEFINITIONS ###

G = 6.67408E-11                                                     # Gravitational constant [m^3/(kg*s^2)]
M = 1.989E30                                                        # Mass of Sun [kg]
c = 3.0E8                                                           # Speed of light [m/s]
au = 1.496E11                                                       # au to m conversion [m]

dl = 550.0 * au                                                     # Distance between lens and observer [m]
ds = 6.0E6 * au                                                     # Distance between source and observer [m]

print("Einstein radius: ", aux.einrad(dl,ds))

img_px = 5000                                                       # Pixels in image plane
src_px = 2500                                                       # Pixels in source plane

extent_img = 1.0                               # Size of image plane covered [rad]
extent_src = 1.0                               # Size of source plane covered [rad]

### LENS PARAMETERS ###

xlens = 0.0                                                         # Lens x-position
ylens = 0.0                                                         # Lens y-position
mlens = 1.0                                                           # Lens mass [M_sun]

xs = 2.0 * extent_img / (img_px - 1)                               # Pixel size on image map
ys = 2.0 * extent_src / (src_px - 1)                               # Pixel size on source map

### SOURCE PARAMETERS ###

xpos = 0.0                                                          # Source x-position
ypos = 0.0                                                          # Source y-position
rad = aux.einrad(dl,ds)*float(np.arctan(6.4E5/9.3E17))                     # Source size (units of einrad)
print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',rad)
# Convert to pixels

ipos = int(round(xpos / ys))                                                    # x (einrad) --> i (px)
jpos = int(round(-ypos / ys))                                                   # y (einrad) --> j (px)
rpix = rad / ys                                                  # r (einrad) --> r (px)

# Make source, image planes

src = aux.cgs(src_px,rpix,jpos,ipos)                                # Source plane (2D Gaussian)
b = np.zeros((img_px,img_px))                                       # Image plane (initialized as empty)

# Field of view variables

c = 0                                                               # Number of pixels of planet seen by Einstein ring
fov = 0                                                             # Percent of planet seen by Einstein ring

### RAYTRACER ###

j1, j2 = np.mgrid[0:img_px,0:img_px]
x1 = -extent_img + j2 * xs                                          #
x2 = -extent_img + j1 * xs

y1, y2 = aux.pt_lens(x1, x2, xlens+0.1, ylens, mlens)
i2 = np.round((y1 + extent_src) / ys)
i1 = np.round((y2 + extent_src) / ys)

ind = (i1 >= 0) & (i1 < src_px) & (i2 >= 0) & (i2 < src_px)

i1n = i1[ind]
i2n = i2[ind]
j1n = j1[ind]
j2n = j2[ind]

for i in np.arange(np.size(i1n)):
    b[int(j1n[i]),int(j2n[i])] = src[int(i1n[i]),int(i2n[i])]
    c += 1


fov = float(c / (src_px * src_px))*100.0


### PLOT ###

fig = plt.figure(1)
ax = plt.subplot(121)
ax.imshow(aux.cgs(src_px,rpix,jpos,ipos), extent = (-extent_src,extent_src,-extent_src,extent_src),cmap='hot')
ax.set_title('Mag = 0')

ax = plt.subplot(122)
ax.imshow(b, extent = (-extent_img,extent_img,-extent_img,extent_img),cmap='hot')
ax.set_title('Mag = ' + str(round(aux.mag(1.0E-6,8.228E13,0)*1.0E-10,2)) + r'x$10^{10}$')
ax.set_xlabel('FOV = ' + str(np.round(fov,2)) + '%')

plt.show()
