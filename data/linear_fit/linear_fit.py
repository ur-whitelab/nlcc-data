import numpy as np
import os
import matplotlib.pyplot as plt

# load data
x, y = np.loadtxt(os.path.join(_FILE_DIR_,'input.dat'), usecols=(0,1), unpack=True)


m = (np.mean(x*y) - np.mean(x)*np.mean(y))/np.std(x)**2
print("slope =", m)

c = np.mean(y) - m*np.mean(x)
print("intercept =", c)

x_n  = np.linspace(min(x), max(x), 50, endpoint=True)
y_n = m*x_n + c

"""
plt.figure()
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y, 'o', label='input')
plt.plot(x_n, y_n, '-', label='output')
plt.title('Linear least square fitting')
plt.legend()
plt.show()
"""

m_cod, c_cod = linear_fit(x,y)

# check
if abs(m - m_cod) and abs(c - c_cod) <= 1e-2:
    result = True
else:
    result = False
    
