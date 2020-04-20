import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci
import math
import random
from astropy.io.fits import getdata


### CONSTANTS ###

G = 6.67408E-11                                                                     # Gravitational constant [m^3/(kg*s^2)]
M = 1.989E30                                                                        # Mass of Sun [kg]
c = 3.0E8                                                                           # Speed of light [m/s]
R = 6.955E8                                                                         # Radius of sun [m]

### DEFINITIONS ###

rg = (2.0*G*M)/(c**2)                                                               # Schwarzschild radius of Sun [m]
z0 = 8.228E13
theta_gr0 = (-2 * rg) / R

### EINSTEIN RADIUS ###

def einrad(dl,ds):
    eta = np.sqrt((4*G*M)/c**2)
    return float(eta * np.sqrt((ds-dl)/(ds*dl)))

### HOMOGENOUS CIRCULAR SOURCE ###

def circ(ny,rad,x1=0.0,y1=0.0):
 x,y=np.mgrid[0:ny,0:ny]
 r2=(x-x1-ny/2)**2+(y-y1-ny/2)**2
 a=(r2<rad**2)
 return a/a.sum()

### CIRCULAR GAUSSIAN SOURCE ###

def cgs(res, sigma, pxx, pxy):
    x,y = np.mgrid[0:res,0:res]
    size = (x - pxx - res / 2.0)**2 + (y - pxy - res / 2.0)**2
    a = np.exp(-size * 0.5 / sigma**2)
    return a/a.sum()

### POINT LENS ###

def pt_lens(x1,x2,x1l,x2l,ml):
    x1ml = (x1 - x1l)
    x2ml = (x2 - x2l)
    d = x1ml**2 + x2ml**2 + 1.0E-12
    y1 = x1 - ml*(x1-x1l)/d
    y2 = x2 - ml*(x2-x2l)/d
    return(y1,y2)

### SINGULAR ISOTHERMAL SPHERE ###

def sis(x1,x2,x1l,x2l,dl,ds):
    x1ml = (x1 - x1l)
    x2ml = (x2 - x2l)
    d = np.sqrt(x1ml**2+x2ml**2+1.0E-12)
    y1 = x1 - einrad(dl,ds)*(x1-x1l) / d
    y2 = x2 - einrad(dl,ds)*(x2-x2l) / d
    return(y1,y2)

### GRAVITATIONAL DEFLECTION ANGLE ###

def theta_gr(b):
    return(theta_gr0 * (R / float(b)))

### MAGNIFICATION ###

def mag(lam,z,p):                                                                   # Magnification as a function of wavelength, lens distance and optical offset
    a = (((2.0 * math.pi)/(lam))*(math.sqrt(2*rg/z))) * p                           # Dimensionless Bessel variable
    return(4.0 * math.pi**2 * (rg / lam) * sci.jv(0,a)**2)

### GAIN ###

def gain(lam,z,p):                                                                  # Gain as a function of wavelength, lens distance and optical offset
    return(10 * np.log10(amp(lam,z,p)))

### FOR OPENING FITS FILES ###

def fitsim(filename):
    a = getdata(filename)
    if (len(a.shape) > 2):
        a = a[0]
    return((1.0*a)/a.sum())
