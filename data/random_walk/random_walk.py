import numpy as np
nlcc_list = np.array(random_walk(100,1.0,3))
#print("trj:",nlcc_list)
second_moment = np.sum(nlcc_list[-1]*nlcc_list[-1])
ideal = 100*(1.0**2)*3
print("second moment:",second_moment)
result = True if np.abs((second_moment-ideal)/ideal) < 0.01 else False
