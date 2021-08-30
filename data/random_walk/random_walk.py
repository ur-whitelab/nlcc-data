import numpy as np
nlcc_list = np.array(random_walk(10000,2.0,3))
second_moment = np.sum(nlcc_list*nlcc_list,axis=-1)
a,b = np.polyfit(np.arange(10001),second_moment)
ideal = 3.0 * (2.0**2)
print("a =",a,", b =",b)
result = True if np.abs((a-ideal)/ideal) < 0.01 else False
