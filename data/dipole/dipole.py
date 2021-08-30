import numpy as np
import os
coordinates = np.loadtxt(os.path.join(_FILE_DIR_,"water.xyz"),usecols=(1,2,3))
#note, these are fake
charges = np.loadtxt(os.path.join(_FILE_DIR_,"charges.txt"))
my_dipole = (coordinates.T*charges).sum(axis=1)
nl_dipole = dipole_moment(coordinates,charges) 

#print("My result:",my_dipole)
#print("NL result:",nl_dipole)
result = True if np.all(np.abs( my_dipole - nl_dipole )<0.01) else False
