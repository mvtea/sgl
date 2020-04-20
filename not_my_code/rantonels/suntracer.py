'''
FILE: suntracer.py
AUTHOR: Mason Tea
PURPOSE: A general relativistic raytracing model of the Solar Gravity Lens. This
         code is an edited version of rantonels' starless code
         (https://rantonels.github.io/)for raytracing black holes, adapted to
         accomodate new parameters for modeling less dramatic systems, like the SGL.

         This program is written in Python 3. Documentation can be found in readme.txt.
'''

#-----------------------------------
# Libraries
#-----------------------------------

# An astronomer's favorites
import numpy as np
import matplotlib.pyplot as plt

# Scipy
import scipy.ndimage as ndim # Multidimensional image procesing
import scipy.misc as spm # Miscellaneous routines

# System
import random, sys, time, os
import datetime

# rantonels utilizes a CPU-based multiprocessing tracer, so we will do the same
import multiprocessing as multi
import ctypes # Allows use of C datatypes

# File parser
import configparser

# Functions written by rantonels -- a blackbody model and an airy disc model
import blackbody as bb
import bloom

# Garbage collector
import gc

# Terminal tools
import curses

#-----------------------------------
# Initialization
#-----------------------------------

# Define conditions for numerical integration methods, Leapfrog and Runge-Kutta (default) integration
method_LF = False
method_RK = True

# Low fidelity render set False by default
lofi = False

# Pixel shuffling in render & matplotlib preview window auto-display arguments
disable_display = False
disable_shuffling = False

# Number of processes to run at once (should equal number of cores in CPU for best results)
threads = 4

# Output plot of scene by default
graph = True

# Resolution override argument set False by default
override_res = False

# Path of default scene to render when given no .scene file as an argument
scene = 'scenes/default.scene'

# Default chunk size (rantonels suggests 2000 or 9000)
chunk_size = 9000

# Change defaults and set parameters based on inline arguments
for arg in sys.argv[1:]:

    # Lofi/hifi render
    if arg == '-lofi':
        lofi = True
        print("Lofi enabled")
        continue

    # Print plot
    if arg == '-nograph':
        graph = False
        print("Graph disabled")
        continue

    # Pixel shuffling
    if arg == '-noshuffle':
        disable_shuffling = True
        print("Shuffling disabled")
        continue

    # Setting for high-performance renders
    if arg == '-hd':
        graph = False
        disable_display = True
        disable_shuffling = True
        print("High-performance mode enabled")
        continue

    # Change chunk size with -c<size>
    if arg[0:2] == '-c':
        chunk_size = int(arg[2:])
        print("Chunk size set to " + str(int(arg[2:])))
        continue

    # Change number of threads (simultaneous processes) with -j<threads>
    if arg[0:2] == '-t':
        threads = int(arg[2:])
        print("Thread count set to " + str(int(arg[2:])))

    # Change resolution with -r<value>x<value>
    if arg[0:2] == '-r':
        override_res = True
        resolution = [int(x) for x in arg[2:].split('x')]

        # Push format error and exit
        if len(resolution) != 2:
            print("ERROR: Unrecognized resolution format; try -r<value>x<value>")
            exit()

        continue

    scene = arg

# Check that the scene path is valid
if not os.path.isfile(scene):
    print("Scene file \"%s\" does not exist: " + str(scene))
    exit()

defaults = {

}
