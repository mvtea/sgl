# Import libraries

from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt

#Initialize constants and variables

n = 0

G =6.67408e-11
c = 3e8
m_au = 149597870700   

m_sun = 1.989e30
r_sun = 695700000
sch_sun = (2 * G * m_sun) / (c**2)
f_sun = (r_sun**2 / (2*sch_sun)) / m_au

r = r_sun
list_r = []
while r <= 49*r_sun:
    list_r.append(r)
    r += r_sun

m = m_sun
list_m = []
while m <= 50*m_sun:
    list_m.append(m)
    m += m_sun

sch = sch_sun
list_sch = []
while n <= 48:
    list_sch.append((2*G*list_m[n])/c**2)
    n += 1

n = 0
f = f_sun
list_f = []
while n <= 48:
    list_f.append((list_r[n]**2 / (2*list_sch[n])) / m_au)
    n += 1

plt.plot(list_f, list_m)
plt.xlabel("Focal distance [au]")
plt.ylabel("Stellar Mass")
plt.show()

plt.plot(list_f, list_r)
plt.xlabel("Focal Distance [au]")
plt.ylabel("Stellar Radius")
plt.show()
