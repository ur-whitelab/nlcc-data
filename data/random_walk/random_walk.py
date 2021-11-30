import numpy as np
import pylab as plt
nsteps = 5000
n_repeats = 250
nlcc_trj_list = []
for i in range(n_repeats):
    nlcc_trj = random_walk(nsteps)
    nlcc_trj_list.append(nlcc_trj)
nlcc_trj_list = np.array(nlcc_trj_list)

msd = (nlcc_trj_list*nlcc_trj_list).mean(axis=0)

a,b = np.polyfit(np.log(np.arange(1,nsteps)),np.log(msd[1:]),1)
#plt.plot(np.arange(nsteps),msd)
#plt.plot(np.arange(nsteps),np.exp(b+a*np.log(np.arange(nsteps))),linestyle='--',label='fit')
#plt.legend()
#plt.show()
#print("a =",a)
#print("b =",b)

#ideal exponent for msd is 1
ideal = 1.0
result = True if np.abs((a-ideal)/ideal) < 0.1 else False
