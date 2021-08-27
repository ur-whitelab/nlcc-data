import numpy as np
nlcc_list = np.array(random_walk(100,1.0,3))
print(nlcc_list)
second_moment = np.sum(nlcc_list*nlcc_list)
result = True if second_moment == 100*(1.0**2)*3 else False
