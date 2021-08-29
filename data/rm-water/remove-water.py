import numpy as np
import mdtraj as md 

traj = md.load('trp-cage-small.trr', top='trp-cage.pdb')
nowater = traj.remove_solvent()
nowater.save('nowater.h5')
newtraj = md.load('nowater.h5')
result = True if newtraj.n_atoms == 284  else False
