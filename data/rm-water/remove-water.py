import os
import mdtraj as md 

traj = md.load('trp-cage-small.trr', top='trp-cage.pdb')
nowater = traj.remove_solvent()
result = True if remove_water(os.path.join(os.getcwd(),'trp-cage-small.trr'),os.path.join(os.getcwd(),'trp-cage.pdb')).n_atoms == nowater.n_atoms else False 
#result = True if remove_water('trp-cage-small.trr','trp-cage.pdb').n_atoms == nowater.n_atoms else False
