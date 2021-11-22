import numpy as np
import sys
import os
import mdtraj as md

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")
trj = md.load(pdb_file)

def my_rmsd_aligned(trj):
    alignment = trj.superpose(trj,0)
    rmsd=md.rmsd(alignment, alignment, 0, precentered=True)
    return rmsd

my_rmsd = my_rmsd_aligned(trj)
nlcc_trj = get_aligned_trj(trj, 0)
nlcc_rmsd = md.rmsd(nlcc_trj, nlcc_trj, 0, precentered=True)

print("My result:", my_rmsd)
print("nlcc result", nlcc_rmsd)

result = True if np.abs( my_rmsd - nlcc_rmsd )<0.1 else False


