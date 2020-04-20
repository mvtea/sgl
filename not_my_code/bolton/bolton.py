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

m.get_backend()


# Package some image display preferences in a dictionary object, for use below:
myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.gray}
#myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.gray}

# Make some x and y coordinate images:
nx = 501
ny = 501
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

# Have a look at the un-lensed Gaussian image:
g_image = ldf.gauss_2d(x, y, gpar)
f = p.imshow(g_image, **myargs)
# IMPORTANT: Kill these imshow GUIs before redisplaying, or you will get bad memory leaks!
# You can kill it with the "red button", or with the following command:
#p.close(f.get_figure().number)
# Alternatively, if you do the following you will probably be OK redisplaying
# without killing the GUI:
#f.axes.hold(False)
p.show()
