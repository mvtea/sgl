import numpy as np
import matplotlib.pyplot as plt
import aux as a


### DEFINITIONS ###

nx = 801                                                            # Pixels in image plane
ny = 801                                                            # Pixels in source plane

xl = 5.0                                                            # Size of image plane covered (theta_E)
yl = 5.0                                                            # Size of source plane covered (theta_E)

### LENS PARAMETERS ###

xlens = 0.0                                                         # Lens x-position
ylens = 0.0                                                         # Lens y-position
mlens = 20.0                                                        # Lens mass (affects Einstein radius)

xs = 2.0 * xl / (nx - 1)                                            # Pixel size on image map
ys = 2.0 * yl / (ny - 1)                                            # Pixel size on source map

# x and y positions of source (circle of radius 0.4)

rad = 0.1

x_lst = np.arange(-1,1,0.1)
y_lst = np.zeros(len(x_lst))


count = 1
for m in range(len(x_lst)):
    ipos = int(round(x_lst[m] / ys))
    jpos = int(round(-y_lst[m] / ys))
    rpix = int(round(rad / ys))

    src = a.cgs(ny,rpix,jpos,ipos)
    b = np.zeros((nx,nx))

    j1, j2 = np.mgrid[0:nx,0:nx]
    x1 = -xl + j2 * xs
    x2 = -xl + j1 * xs

    y1, y2 = a.pt_lens(x1, x2, xlens+0.1, ylens, mlens)
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

    plt.imshow(b, extent = (-xl,xl,-xl,xl))
    fb = np.sum(b) * (xs**2)/(ys**2)
    plt.title('Flux = ' + str(fb))

    plt.savefig('fig%1d' % count)
    count += 1


'''
-----------------------------
'''

                                                      # Source size

                                            # Image plane

### RAYTRACER ###



'''
NEXT STEPS:

    - Add magnification, SNR data, PSF spread
    - Optimize for SGL
    - Interactability

    1. Directly from source to lensed image
    2. Implement magnification, gain, point-spreading
    3. ........

'''
