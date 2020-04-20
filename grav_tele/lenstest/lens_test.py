#
# lensdemo_script.py
#
# A script to allow simple explortation of gravitational lensing
# of extended objects (i.e., galaxies) by the gravity of a singular
# isothermal ellipsoid (SIE) potential.
#
# This script is meant to be used as a cut-and-paste guide to an interactive
# python2.5 command-line session, and is not necessarily to be run in
# unmodified form from end to end.
#
# Requires numpy and matplotlib, as well as the suporting file "lensdemo_funcs.py"
#
# Copyright 2009 by Adam S. Bolton
# Creative Commons Attribution-Noncommercial-ShareAlike 3.0 license applies:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# All redistributions, modified or otherwise, must include this
# original copyright notice, licensing statement, and disclaimer.
# DISCLAIMER: ABSOLUTELY NO WARRANTY EXPRESS OR IMPLIED.
# AUTHOR ASSUMES NO LIABILITY IN CONNECTION WITH THIS COMPUTER CODE.
#

# Import the necessary packages
import numpy as n
import matplotlib as m
# The following 2 lines are necessary to make the
# GUI work right, at least for me. YMMV!
m.use('TkAgg')
m.interactive(True)
from matplotlib import pyplot as p
from matplotlib import cm
import lensdemo_funcs as ldf

# Package some image display preferences in a dictionary object, for use below:
myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.spectral}
#myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.gray}

# Make some x and y coordinate images:
nx = 1001
ny = 1001
xhilo = [-2.5, 2.5]
yhilo = [-2.5, 2.5]
x = (xhilo[1] - xhilo[0]) * n.outer(n.ones(ny), n.arange(nx)) / float(nx-1) + xhilo[0]
y = (yhilo[1] - yhilo[0]) * n.outer(n.arange(ny), n.ones(nx)) / float(ny-1) + yhilo[0]

# Set some Gaussian blob image parameters and pack them into an array:
g_amp = 1.0   # peak brightness value
g_sig = 0.05  # Gaussian "sigma" (i.e., size)
g_xcen = 0.0  # x position of center
g_ycen = 0.0  # y position of center
g_axrat = 1.0 # minor-to-major axis ratio
g_pa = 0.0    # major-axis position angle (degrees) c.c.w. from x axis
gpar = n.asarray([g_amp, g_sig, g_xcen, g_ycen, g_axrat, g_pa])


# Set some SIE lens-model parameters and pack them into an array:
l_amp = 1.5   # Einstein radius
l_xcen = 0.0  # x position of center
l_ycen = 0.0  # y position of center
l_axrat = 1.0 # minor-to-major axis ratio
l_pa = 0.0    # major-axis position angle (degrees) c.c.w. from x axis
lpar = n.asarray([l_amp, l_xcen, l_ycen, l_axrat, l_pa])

# Compute the lensing potential gradients:
(xg, yg) = ldf.sie_grad(x, y, lpar)

# Evaluate lensed Gaussian image:
g_lensimage = ldf.gauss_2d(x-xg, y-yg, gpar)

# Have a look:
f = p.imshow(g_lensimage, **myargs)

p.savefig('lens_xy1001.png')

n.savetxt("pixel_data_1001.txt", g_lensimage, fmt='%d', delimiter=' ')
