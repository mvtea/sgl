#Program to compute the minimum focal distance of light passing the sun at a distance equal to the
#radius of the sun

import matplotlib.pyplot as plt

#Constants

G = 6.67e-11              #Gravitational constant [m^3 kg^-1 s^-2]
M_sun = 1.989e30          #Mass of the sun [kg]
c = 3e8                   #Speed of light [m/s]
r_sun = 695500000         #Radius of the sun [m]
m_per_km = 1000           #Meters per kilometer
m_per_pc = 3.086e16       #Meters per parsec
m_per_au = 149597870700   #Meters per astronomical unit

#Calculations

alpha = (4 * G * M_sun) / (c**2 * r_sun)      #Light deflection angle at the radius of the sun
d_focal_m = r_sun / alpha                     #Minimum focal distance of telescope [m]

#Conversions

d_focal_pc = d_focal_m / m_per_pc       #Convert minimum focal distance from meters to parsecs [pc]
d_focal_km = d_focal_m / m_per_km       #Convert minimum focal distance from meters to kilometers [km]
d_focal_au = d_focal_m / m_per_au       #Convert minimum focal distance from meters to au

#Terminal

print("")
print ("Minimum focal distance in meters = %r" % d_focal_m)
print ("Minimum focal distance in kilometers = %r" % d_focal_km)
print ("Minimum focal distance in parsecs = %r" % d_focal_pc)
print ("Minimum focal distance in astronomical units = %r" % d_focal_au)

#Program to compute focal distance at different radii & deflection angles

#Variables

dr = 1
r = r_sun
list_r = []
list_d = []

#Calculations

print ("")
print ("Focal distances for radii ranging from sun's radius to 1.1x sun's radius (au)")
print ("")

while dr < 1.1:
  r = r_sun * dr
  list_r.append(r)
  alpha_r = (4 * G * M_sun) / (c**2 * r)
  d_focal_r = r / alpha_r
  d_focal_r_au = d_focal_r / m_per_au
  print ("%r au" % d_focal_r_au)
  dr += .01
  list_d.append(d_focal_r_au)

print("")

#Plot data in two lists

#plt.plot(list_x, list_y)
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()

#Program to compute and plot critical frequency of light passing through the
#sun's atmosphere and the impact parameter of the light's path
