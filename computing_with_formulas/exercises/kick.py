"""Compute the air resistance on a football.
The drag force, due to air resistance, on an object can be expressed
as
    
    Fd = 1/2 * C_D * q * A * V**2 ,

    where q is the density of the air, V is the velocity of the object, A is
the cross-sectional area (normal to the velocity direction), and C D is
the drag coefficient, which depends heavily on the shape of the object
and the roughness of the surface."""

from math import pi

C_D = 0.2       # drag coefficient
a = 11          # radius of the ball as cm for a football
phr = 1.2       # density of air (m^-3)
m = 0.43        # mass of the ball in kg
g = 9.81        # Gravitational acceleration (ms^-2)
A = pi * a**2
F_g = m*g

speed_conversation = 1000 / 3600
    
V = 120 * speed_conversation        # calculate the forces on the ball for a hard kick
F_d = 1/2 * C_D * phr * A * V**2
print('For a hard kick forces is: (v=%g) the drag force is: %g and \
        the gravitiy force is: %g' % (V, F_d, F_g))
