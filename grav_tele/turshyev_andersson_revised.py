'''

This program is a revised version of grav_tele_composite. It is meant to compute values and create
figures relevant to the focal distance of the proposed solar gravitational telescope.

'''

# Import libraries

from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt

# Initialize constants and variables

G = 6.67408e-11                             # Gravitational constant [m^3 kg^-1 s^-2]
M_sun = 1.989e30*(.1221)                            # Mass of the sun [kg]
c = 3e8                                     # Speed of light [m/s]
r_sun = 695500000*(.1542)                      # Radius of the sun [m]

m_per_au = 149597870700                     # Meters per astronomical unit [m / au]

schwarz_sun = (2 * G * M_sun) / c**2        # Schwarzchild radius of the sun [m]


# Initialize constant lists

b = r_sun                                   # Impact parameter counter [m]
db = 0.01 * r_sun                           # Increase in b of 1% of the sun's radius

list_b = []                                 # List of impact parameters
                                            
while b <= 6 * r_sun:                       # Create a list of all values for the impact
    list_b.append(b)                        # parameter, b, from the sun's radius to the sun's
    b += db                                 # diameter, at increments of 1% the sun's radius
    
b = r_sun                                   # Reset impact parameter counter [m]
n = 0                                       # List element counter

list_b_r = []                               # List of impact parameter / sun radius ratios

while b <= 6 * r_sun:                       # Create a list of all values for ratios of 
    list_b_r.append(list_b[n] / r_sun)      # the impact parameter to the sun's radius
    b += db                                 
    n += 1

# Equation (1)
# Compute deflection angle of light due to the sun's gravity [rad]

theta_gr_0 = -(2 * schwarz_sun) / r_sun     # Deflection angle at solar limb (b = 0) [rad]

list_theta_gr_b = []                        # List of deflection angles due to gravity at
                                            # impact parameters from 1x - 6x the sun's radius
n = 0

while n <= 500:
    theta_gr_b = theta_gr_0 * (r_sun / list_b[n])
    list_theta_gr_b.append(theta_gr_b)
    n += 1


# Equation (2)
#Compute focal distances for different impact parameters independent of solar plasma interference

f_0 = (r_sun**2 / (2 * schwarz_sun)) / m_per_au          # Minimum focal distance [au]


list_f_b = []

n = 0

while n <= 500:
    f_b = f_0 * (list_b[n]**2 / r_sun**2)
    list_f_b.append(f_b)
    n += 1



# Equation (13)
# Compute refraction angles due to plasma interference at specific frequencies & varying
# impact parameter; near-IR (430 THz) and near-UV (770 THz)

v_0 = 6.32
v_near_IR = 4.3e8
v_near_UV = 7.7e8
v_xband = 8000
v_kband = 26000 

list_theta_pl_near_IR = []
list_theta_pl_near_UV = []

list_theta_pl_xband = []
list_theta_pl_kband = []

n = 0

while n <= 500:
    theta_pl_near_IR = (v_0 / v_near_IR)**2 * (2952 * (r_sun / list_b[n])**16 + 228 * (r_sun / list_b[n])**6 + 1.1 * (r_sun / list_b[n])**2)
    theta_pl_near_UV = (v_0 / v_near_UV)**2 * (2952 * (r_sun / list_b[n])**16 + 228 * (r_sun / list_b[n])**6 + 1.1 * (r_sun / list_b[n])**2)
    theta_pl_xband = (v_0 / v_xband)**2 * (2952 * (r_sun / list_b[n])**16 + 228 * (r_sun / list_b[n])**6 + 1.1 * (r_sun / list_b[n])**2)
    theta_pl_kband = (v_0 / v_kband)**2 * (2952 * (r_sun / list_b[n])**16 + 228 * (r_sun / list_b[n])**6 + 1.1 * (r_sun / list_b[n])**2)
    list_theta_pl_near_IR.append(theta_pl_near_IR)
    list_theta_pl_near_UV.append(theta_pl_near_UV)
    list_theta_pl_xband.append(theta_pl_xband)
    list_theta_pl_kband.append(theta_pl_kband)
    n += 1
    
# Create list of log10(theta) for plot

list_theta_pl_near_IR_log = []
list_theta_pl_near_UV_log = []
list_theta_gr_b_log = []
list_theta_pl_xband_log = []
list_theta_pl_kband_log = []

n = 0

while n <= 500:
    list_theta_pl_near_IR_log.append(math.log(list_theta_pl_near_IR[n], 10))
    list_theta_pl_near_UV_log.append(math.log(list_theta_pl_near_UV[n], 10))
    list_theta_gr_b_log.append(math.log(math.fabs(list_theta_gr_b[n]), 10))
    list_theta_pl_xband_log.append(math.log(list_theta_pl_xband[n], 10))
    list_theta_pl_kband_log.append(math.log(list_theta_pl_kband[n], 10))
    n += 1
    
# Plot  plasma refraction against impact parameter

plt.plot(list_b_r, list_theta_pl_near_IR_log)
plt.plot(list_b_r, list_theta_pl_near_UV_log)
plt.plot(list_b_r, list_theta_gr_b_log)
plt.plot(list_b_r, list_theta_pl_xband_log)
plt.plot(list_b_r, list_theta_pl_kband_log)
plt.xlabel("IMPACT PARAMETER, b[r_sun]")
plt.ylabel("PLASMA REFRACTION ANGLE, log10(theta_pl) [rad]")
plt.xlim(0.9, 6.1)
plt.ylim(-18, 0)
plt.show()



# Equation (15)
# Focal distance taking into account plasma interference

list_f_tot_near_IR = []
list_f_tot_near_UV = []

n = 0

while n <= 500:
    f_tot_near_IR = f_0 * list_b_r[n]**2 * (1 - (r_sun / (2 * schwarz_sun)) * list_b_r[n] * list_theta_pl_near_IR[n])**-1
    f_tot_near_UV = f_0 * list_b_r[n]**2 * (1 - (r_sun / (2 * schwarz_sun)) * list_b_r[n] * list_theta_pl_near_UV[n])**-1
    list_f_tot_near_IR.append(f_tot_near_IR)
    list_f_tot_near_UV.append(f_tot_near_UV)
    n += 1

plt.plot(list_b_r, list_f_tot_near_IR)
plt.plot(list_b_r, list_f_tot_near_UV)
plt.xlabel("IMPACT PARAMETER, B[R_SUN]")
plt.ylabel("EFFECTIVE DISTANCE [AU]")
plt.show()

# ADD EQUATION FOR FOCUS TAKING INTO ACCOUNT PLASMA INTERFERENCE
# ADD CURVE FOR FOCAL DISTANCE (GR + PL) VS IMPACT PARAMETER

# DATA IMPLIES CONSTANT FOCAL DISTANCE
