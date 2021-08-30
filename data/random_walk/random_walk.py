import numpy as np
# run 100 times
nlcc_trj_list = []
for i in range(100):
    nlcc_trj = random_walk(20000,1.0,2)
    nlcc_trj_list.append(nlcc_trj)
nlcc_trj_list = np.array(nlcc_trj_list)
print("random walk shape:",nlcc_trj_list.shape)
second_moment = np.sum(nlcc_trj_list*nlcc_trj_list,axis=-1)
#a,b = np.polyfit(np.arange(20000)[10000:],second_moment[10000:],1)
#print("a =",a,", b =",b)
a = np.mean(second_moment[10000:] / np.arange(20000)[10000:])
print("a =",a)
ideal = 2.0
result = True if np.abs((a-ideal)/ideal) < 0.1 else False
