"""How to cook perfect egg."""

from math import pi, log

T_W = 373.15    # temperature of the boiling water
T_O = 277.15    # tempreature of the egg before being put in the water
T_Y = 343.15
M = 0.067       # M - tha mass for small egg
p = 1.038 * 1000       # The density
c = 3.7         # the specific heat capacity
K = 0.54         # the termal conductivity

# large egg taken from the fridge temperature
t = M**(2/3) * c*p **(1/3) / (K*pi**2 * (4*pi/3)**(2/3)) \
    * log(0.76 *(T_O - T_W) / (T_Y - T_W))

print('The t(time) that takes (in seconds) for center of the yolk')
print('to reach the temperature (T_Y) (in Celsius degrees)')
print('Computed t (%g) for a large egg taken from the fridge (T_O = %.2f C)' % (t, T_O))

# large egg taken from the room temperature
T_O = 20
t = (((M)**2/3 * (c*p)**1/3) / (((K*pi)**2) * (4*pi/3)**2/3)) \
    * log(0.76 *(T_O - T_W) / (T_Y - T_W))
print('Computed t (%g) for a large egg taken from room temperature(T_O = %.2f C)' % (t, T_O))
