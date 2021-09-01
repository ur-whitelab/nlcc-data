import numpy as np

def cal_func(x,y,z):
    """
    This function is a sphere.
    """
    #f = x**2 + y**2 + z**2 
    f = x**3 + y**3 + z**3
    return f


f_data = np.empty((21,21,21), dtype=float)

for x in range(-10, 11, 1):
    for y in range(-10, 11, 1):
        for z in range(-10, 11, 1):
            f_data[x,y,z] = cal_func(x,y,z)


# input params
n = 3
ax= 0
dx = 1

# making a copy
f_data_copy = f_data.copy()

# calculating the nth order derivative along ax with spacing dx
for i in range(n):
    f_der_xi = np.gradient(f_data_copy, dx, axis=ax)
    f_data_copy = f_der_xi.copy()


# check
if np.all(f_der_xi == gradient(f_data, n, ax, dx)):
    result = True
else:
    result = False

