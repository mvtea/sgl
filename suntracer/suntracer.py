'''
FILE: suntracer.py
AUTHOR: Mason V. Tea, Wesleyan University '21
PURPOSE: SunTracer is a raytracing simulation for strong gravitational lensing
         as seen by the Solar Gravitational Lens (SGL).
'''

### LIBRARIES ###

import numpy as np
import matplotlib.pyplot as plt

import aux                                  # Auxiliary functions

### PLANE PARAMETERS ###

n_img = 1001                                # Pixels in image plane
n_src = 1001                                 # Pixels in source plane

                                            # (UNITS OF EINSTEIN RADIUS)
rmap_img = 2.0                              # Radius of image plane in plot
rmap_src = 2.0                              # Radius of source plane in plot

px_img = 2.0 * rmap_img / (n_img - 1)       # Pixel size on image map
px_src = 2.0 * rmap_src / (n_src - 1)       # Pixel size on source map

### SOURCE & LENS PARAMETERS ###

# Source #

x_src = 0.0                                 # X-coordinate of source
y_src = 0.0                                 # Y-coordinate of source
r_src = 0.05                                 # Radius of source (einrad)

# Lens #

x_lens = 0.0                                # X-coordinate of lens
y_lens = 0.0                                # Y-coordinate of lens
m_lens = 1.0                                # Mass of lens

# Pixel conversion #

i_src = int(round(x_src/px_src))            # X-position of source in pixels
j_src = int(round(y_src/px_src))            # Y-position of source in pixels
rpix_src = int(round(r_src/px_src))         # Radius of source in pixels

# Source and image plane #

src_plane = aux.cgs(n_src,rpix_src,i_src,j_src)     # Source is circular gaussian
img_plane = np.zeros((n_img,n_img))                 # Image plane is empty

### RAYTRACE ###

mapped = 0
unmapped = 0

for a in range(n_img):
    for b in range(n_img):
        # Image pixels to coordinates
        x_coord = -rmap_img + b * px_img
        y_coord = -rmap_img + a * px_img

        # Deflection by point source
        x_def, y_def = aux.pt_lens(x_coord,y_coord,x_lens,y_lens,m_lens)

        # Coordinates back to pixels
        y_px = int(round((x_def + rmap_src) / px_src))
        x_px = int(round((y_def + rmap_src) / px_src))

        # If a ray hits a pixel within the source, map that pixel on the image plane
        # and count pixels which do map
        if ((y_px >= 0) and (y_px < n_src) and (x_px >= 0) and (x_px < n_src)):
            img_plane[a,b] = src_plane[x_px,y_px]
            mapped += 1
        else:
            unmapped += 1

### PLOTS ###

plt.subplot(121)
plt.imshow(src_plane, extent=(-rmap_src,rmap_src,-rmap_src,rmap_src), cmap='hot')
plt.subplot(122)
plt.imshow(img_plane, extent=(-rmap_img,rmap_img,-rmap_img,rmap_img), cmap='hot')
plt.show()

print("\nMapped:Unmapped = ", 100.0*float(mapped/(mapped + unmapped)),"\n")
