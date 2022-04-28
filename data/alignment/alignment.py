import numpy as np
import sys
import os
import mdtraj as md

pdb_file = os.path.join(_FILE_DIR_, "1VII_twoframe_shifted.pdb")
trj = md.load(pdb_file)


def myrmsd(trj, frame):
    xyz = trj.xyz
    xyz0 = trj.xyz[frame]
    dx = xyz-xyz0
    dx2 = (dx*dx).sum(axis=2)
    rmsd = np.sqrt(dx2.mean(axis=1))
    return rmsd


#print("Starting rmsd:", myrmsd(trj, 0))
aligned_trj = trj.superpose(trj, 0)

my_rmsd = myrmsd(aligned_trj, 0)
#print("Aligned rmsd:", my_rmsd)

nlcc_trj = align_traj(trj, 0)
nlcc_rmsd = myrmsd(nlcc_trj, 0)

#print("nlcc rmsd", nlcc_rmsd)

result = True if np.all(np.abs(my_rmsd - nlcc_rmsd)) < 0.01 else False
