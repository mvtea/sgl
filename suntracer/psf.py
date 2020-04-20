'''
FILE: psf.py
AUTHOR: Mason Tea
PURPOSE: Calculate and plot SGL point-spreading and gain.
'''

### LIBRARIES ###

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci
from mpl_toolkits import mplot3d
import math

### CONSTANTS ###

G = 6.67408E-11                                                                     # Gravitational constant [m^3/(kg*s^2)]
M = 1.989E30                                                                        # Mass of Sun [kg]
c = 3.0E8                                                                           # Speed of light [m/s]

### DEFINITIONS ###

rg = (2.0*G*M)/(c**2)                                                               # Schwarzschild radius of Sun [m]
z0 = 8.228E13                                                                       # Minimum SGL focal distance (550au) [m]

p = np.arange(-0.5,0.5,0.00001)                                                      # Array representing optical axis offset [m]

### CALCULATIONS ###

def mag(lam,z,p):                                                                   # Magnification as a function of wavelength, lens distance and optical offset
    a = (((2.0 * math.pi)/(lam))*(math.sqrt(2*rg/z))) * p                           # Dimensionless Bessel variable
    return(4.0 * math.pi**2 * (rg / lam) * sci.jv(0,a)**2)

def gain(lam,z,p):                                                                  # Gain as a function of wavelength, lens distance and optical offset
    return(10 * np.log10(mag(lam,z,p)))

### PLOTS ###

# Magnification (visible)

plt.style.use('seaborn-dark')
plt.plot(p*1000,mag(4.0E-9,z0,p)*1.0E-13,label=r'$\lambda$=380nm',color='blueviolet')
plt.plot(p*1000,mag(4.7E-9,z0,p)*1.0E-13,label=r'$\lambda$=470nm',color='b')
plt.plot(p*1000,mag(5.5E-9,z0,p)*1.0E-13,label=r'$\lambda$=565nm',color='g')
plt.plot(p*1000,mag(6.0E-9,z0,p)*1.0E-13,label=r'$\lambda$=580nm',color='yellow')
plt.plot(p*1000,mag(6.3E-9,z0,p)*1.0E-13,label=r'$\lambda$=610nm',color='orange')
plt.plot(p*1000,mag(6.65E-9,z0,p)*1.0E-13,label=r'$\lambda$=740nm',color='r')
plt.title('SGL Magnification vs Optical Axis Offset')
plt.xlabel(r'Distance from optical axis, $\rho$ [cm]')
plt.ylabel(r'Magnification, $\mu$ (x$10^{13}$)')
plt.text(1.2,1.6,r'$D_L$ = 600au')
plt.legend()
plt.savefig('SGL_vis_mag.png')
plt.xlim(0,1.5)
plt.show()
plt.close()

# Magnification (1 micrometer)

plt.style.use('seaborn-dark')
plt.plot(p,mag(1.0E-6,z0,p)*1.0E-11,label=r'$\lambda$=1$\mu$m', color='black')
plt.plot(p,mag(2.0E-6,z0,p)*1.0E-11,label=r'$\lambda$=2$\mu$m', linestyle='-.', color='slategrey')
plt.title('SGL Magnification vs Optical Axis Offset')
plt.xlabel(r'Distance from optical axis, $\rho$ [m]')
plt.ylabel(r'Magnification, $\mu$ (x$10^{11}$)')
plt.text(0.225,0.9,r'$D_L$ = 600au')
plt.legend()
plt.savefig('SGL_mag.png')
plt.xlim(-0.35,0.35)
plt.show()
plt.close()

# Mag "corner" plots

fig,axes= plt.subplots(nrows=3, ncols= 3)
st = fig.suptitle(r'SGL Offset-Amplification at Varying ($\lambda, D_s$)', fontsize="x-large")

fig.text(0.52, -0.03, r'$D_s\longrightarrow$', ha='center')
fig.text(-0.02, 0.48, r'$\lambda\longrightarrow$', va='center', rotation='vertical')

axes[2][0].plot(p,mag(1.0E-6,z0,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[2][1].plot(p,mag(1.0E-6,z0*2,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[2][2].plot(p,mag(1.0E-6,z0*4,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')

axes[1][0].plot(p,mag(2.0E-6,z0,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[1][1].plot(p,mag(2.0E-6,z0*2,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[1][2].plot(p,mag(2.0E-6,z0*4,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')

axes[0][0].plot(p,mag(3.0E-6,z0,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[0][1].plot(p,mag(3.0E-6,z0*2,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')
axes[0][2].plot(p,mag(3.0E-6,z0*4,p)*1.0E-10,label=r'$\lambda$=1$\mu$m')

# shift subplots down:
st.set_y(1.05)
fig.subplots_adjust(top=0.85)

plt.tight_layout()
#plt.show()
plt.close()

# Gain

plt.style.use('seaborn-dark')
plt.plot(p,gain(1.0E-6,z0,p),label=r'$\lambda$=1$\mu$m',color='lightcoral')
plt.plot(p,gain(2.0E-6,z0,p),linestyle='--',label=r'$\lambda$=2$\mu$m',color='firebrick')
plt.title('SGL Gain vs Optical Axis Offset')
plt.xlabel(r'Distance from optical axis, $\rho$ [m]')
plt.ylabel(r'Gain, G($\lambda, D_L$)')
plt.text(-0.5,109,r'$D_L$=600au')
plt.ylim(70,112)
plt.legend()
plt.savefig('SGL_Gain.png')
#plt.show()
plt.close()

fig,axes= plt.subplots(nrows=3, ncols= 3)
st = fig.suptitle(r"SGL Offset-Gain at Varying ($\lambda, D_s$)", fontsize="x-large")

axes[2][0].plot(p,gain(1.0E-6,z0,p),label=r'$\lambda$=1$\mu$m')
axes[2][1].plot(p,gain(1.0E-6,8.975E13,p),label=r'$\lambda$=1$\mu$m')
axes[2][2].plot(p,gain(1.0E-6,9.723E13,p),label=r'$\lambda$=1$\mu$m')

axes[1][0].plot(p,gain(2.0E-6,z0,p),label=r'$\lambda$=1$\mu$m')
axes[1][1].plot(p,gain(2.0E-6,8.975E13,p),label=r'$\lambda$=1$\mu$m')
axes[1][2].plot(p,gain(2.0E-6,9.723E13,p),label=r'$\lambda$=1$\mu$m')

axes[0][0].plot(p,gain(3.0E-6,z0,p),label=r'$\lambda$=1$\mu$m')
axes[0][1].plot(p,gain(3.0E-6,8.975E13,p),label=r'$\lambda$=1$\mu$m')
axes[0][2].plot(p,gain(3.0E-6,9.723E13,p),label=r'$\lambda$=1$\mu$m')

fig.text(0.52, -0.03, r'$D_s\longrightarrow$', ha='center')
fig.text(-0.02, 0.48, r'$\lambda\longrightarrow$', va='center', rotation='vertical')

plt.tight_layout()

# shift subplots down:
st.set_y(0.95)
fig.subplots_adjust(top=0.85)

#plt.show()
plt.close()
