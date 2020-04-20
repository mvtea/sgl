from numpy import *
import matplotlib.pyplot as plt
import math

#Constants

G = 6.67408e-11                 #Gravitational constant [m^3 kg^-1 s^-2]
M_sun = 1.989e30                #Mass of the sun [kg]
c = 3e8                         #Speed of light [m/s]
r_sun = 695500000               #Radius of the sun [m]
m_per_au = 149597870700         #Meters per astronomical unit

# Equation (1)

b = r_sun                       #Impact parameter [m]
db = 0.5 * r_sun                #Change in impact parameter (functional use)

list_b_1 = []                   #Impact parameter function count
list_theta = []                 #Deflection angle function count

schwarz_sun = (2*G*M_sun)/c**2                   #Schwarzchild radius of the sun [m]
theta_gr_naught = -(2*schwarz_sun)/r_sun         #Deflection angle towards the sun due to gravity [radian]

print("")
print("SCHWARZCHILD RADIUS OF THE SUN: %r meters" % round(schwarz_sun, 2))
print("")
print("DEFLECTION ANGLE (independent of impact parameter): %r radians" % round(theta_gr_naught, 8))
print("")

print("DEFLECTION ANGLES FROM b = r_sun to b = 5r_sun:")
print("")

while b <= (5 * r_sun):                            #Compute deflection angles as a function
  theta_gr_b = theta_gr_naught * (r_sun / b)       #of impact parameter from the sun's radius
  list_b_1.append(b)                               #to 1.x the sun's radius
  list_theta.append(theta_gr_b)
  b += db
  print("%r rad" % theta_gr_b)


print("")

#Equation (2)

b = r_sun                                      #Reset impact parameter for second function
db = 0.01 * r_sun
list_b_2 = []                                  #Impact parameter function count
list_f_b = []                                  #Focal distance function count

alpha = (4 * G * M_sun) / (c**2 * r_sun)       #Light deflection angle at the radius of the sun
f_naught_m = r_sun / alpha                     #Minimum focal distance of telescope [m]
f_naught_au = f_naught_m / m_per_au            #Convery focal distance to au

print("MINIMUM FOCAL DISTANCE FROM THE SUN: %r au" % round(f_naught_au, 2))
print("")

print("FOCAL DISTANCES FROM b = r_sun to b = 1.1r_sun:")
print("")

while b <= (1.1 * r_sun):                      #Compute focal distances as a function of
  f_b = f_naught_au * (b**2 / r_sun**2)        #impact parameter from the sun's radius
  list_b_2.append(b)                           #to 1.1x the sun's radius
  list_f_b.append(f_b)
  b += db
  print("%r au" % round(f_b, 2))

print("")

#Equation (13)

b = r_sun                                   #Reset impact parameter for third function
db = .005 * r_sun                           #Change in impact parameter for function counting
v_naught = 6.32                             #Minimum frequency (?) [MHz]
v1 = 4.3e8                                  #Near-infrared frequency "barrier" [MHz]
v2 = 7.7e8                                  #Near-ultraviolet frequency "barrier' [MHz]

list_v1 = []                                #Frequency counter
list_pl1 = []                               #Refraction angle counter
list_b_r1 = []                              #Impact parameter counter

print("CURVES FOR NEAR-INFRARED (BLUE) AND NEAR-ULTRAVIOLET (ORANGE) ARE DISPLAYED")
print("")

#Compute curve for lower limit of deflection angle vs impact parameter (near-infrared)

while b <= 6*r_sun:
  pl = (v_naught / v1)**2 * (2.952e3 * (r_sun / b)**16 + 2.28e2 * (r_sun / b)**6 + 1.1 * (r_sun / b)**2)
  #Refraction angle due to the interference of the photosphere
  list_b_r1.append(b / r_sun)
  list_pl1.append(math.log(pl, 10))
  b += db

b = r_sun            #Reset impact parameter
list_v2 = []         #Frequency counter
list_pl2 = []        #Refraction angle counter
list_b_r2 = []       #Impact parameter counter

#Compute curve for lower limit of deflection angle vs impact parameter (near-ultraviolet)

while b <= 6*r_sun:
  pl = (v_naught / v2)**2 * ((2.952e3 * (r_sun / b)**16) + (2.28e2 * (r_sun / b)**6) + (1.1 * (r_sun / b)**2))
  #Deflection angle due to the interference of the photosphere
  list_b_r2.append(b / r_sun)
  list_pl2.append(math.log(pl, 10))
  b += db

#Compute curve for absolute value of gravitational contribution to light bending

b = r_sun
list_theta_gr_abs = []
list_b_r3 = []

while b <= 6 * r_sun:
  theta_gr_abs = theta_gr_naught * (r_sun / b)
  list_b_r3.append(b / r_sun)
  list_theta_gr_abs.append(math.log(math.fabs(theta_gr_abs)))
  b += db

plt.plot(list_b_r1, list_pl1)
plt.plot(list_b_r2, list_pl2)
plt.plot(list_b_r3, list_theta_gr_abs)
plt.xlabel("IMPACT PARAMETER, b[r_sun]")
plt.ylabel("PLASMA REFRACTION ANGLE, log theta [rad]")
plt.show()

# Equation (16)

b = r_sun
vcrit = 0
v2crit = 0
list_vcrit = []
list_b_r4 = []

while b <= 6 * r_sun:
  v2crit = 2161**2 * (2.952e3 * (r_sun / b)**15 + 2.28e2 * (r_sun / b)**5 + 1.1 * (r_sun / b))
  vcrit = v2crit**0.5 #MHz
  list_b_r4.append(b / r_sun)
  list_vcrit.append(vcrit)
  b += db

plt.plot(list_b_r4, list_vcrit)
plt.xlabel("IMPACT PARAMETER, b[r_sun]")
plt.ylabel("CRITICAL FREQUENCY, v [MHz]")
plt.show()
