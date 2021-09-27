import numpy as np
import math 

# cartesian coordinate
x = 2.0
y = 3.9
z = 4.6

# polar coordiante
r = np.sqrt(x**2+y**2+z**2)
theta = math.acos(z/r)
phi = math.atan(y/x)

# data from codex
r_co, theta_co, phi_co = polar_coord(x,y,z)


# check
if np.allclose([r, theta, phi], [r_co, theta_co, phi_co]) ==  True:
    result = True 
else:
    result = False
