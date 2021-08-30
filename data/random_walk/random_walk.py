import numpy as np
nlcc_list = np.array(random_walk(20000,1.0,2))
print("random walk shape:",nlcc_list.shape)
second_moment = np.sum(nlcc_list*nlcc_list,axis=-1)
#a,b = np.polyfit(np.arange(20000)[10000:],second_moment[10000:],1)
#print("a =",a,", b =",b)
a = np.mean(second_moment[10000:] / np.arange(20000)[10000:])
print("a =",a)
ideal = 2.0
result = True if np.abs((a-ideal)/ideal) < 0.1 else False
