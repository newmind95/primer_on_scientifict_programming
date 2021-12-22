# program for computing the height of the ball thrown in the air
v0 = 5      # initial velocity
g = 9.81    # acceleration of gravity
t = 0.61    # time
y = v0*t - 1/2*g*t**2       # vertical position
print("At t=%g s, the height of the ball is %.2f m." % (t, y))
