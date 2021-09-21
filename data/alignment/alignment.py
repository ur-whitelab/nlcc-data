import numpy as np
import sys
import os

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")

def alingment(pdb_file):
    import mdtraj as md
    pdb = md.load(pdb_file)
    alignment = pdb.superpose(pdb,0)
    return alignment
    rmsd=md.rmsd(pdb,pdb, 0,alignment,precentered=True)



my_rmsd = alingment(pdb_file)
nlcc_rmsd=protein_alignment(pdb_file)

#print("My result:", my_rmsd)
#print("nlcc result", nlcc_rmsd)

result = True if np.abs( my_rmsd - nlcc_rmsd )<0.1 else False


