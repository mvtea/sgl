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

G = 6.67408E-11                                                     # Gravitational constant [m^3/(kg*s^2)]
M = 1.989E30                                                        # Mass of Sun [kg]
c = 3.0E8                                                           # Speed of light [m/s]
au = 1.496E11                                                       # au to m conversion [m]

dl = 550.0 * au                                                     # Distance between lens and observer [m]
ds = 6.0E6 * au                                                     # Distance between source and observer [m]
