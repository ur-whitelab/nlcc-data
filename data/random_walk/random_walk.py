import numpy as np
nlcc_list = np.array(random_walk(20000,2.0,3))
second_moment = np.sum(nlcc_list*nlcc_list,axis=-1)
a,b = np.polyfit(np.arange(20000)[10000:],second_moment[10000:],1)
ideal = 3.0 * (2.0**2)
print("a =",a,", b =",b)
result = True if np.abs((a-ideal)/ideal) < 0.1 else False
