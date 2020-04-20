from astropy.constants import c
from astropy.constants import G
from astropy.cosmology import WMAP9 as cosmology

import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt

import os
import PIL as pil

#import torch
#import refractor

# Source images

images = os.listdir('EPIC')

image = pil.Image.open('EPIC/EPIC_1.png').convert('L')
image_data = np.asarray(image.getdata()).reshape(image.size)

plt.imshow(image_data, interpolation='nearest')
plt.show()
