import numpy as np
import mdtraj as md
import sys

pdb_file=sys.argv[1]

def compute_rg_mdtraj(pdb_file):
    pdb = md.load(pdb_file)
    rg = md.compute_rg(pdb_file)
    return rg

my_rg = compute_rg_mdtraj(pdb_file)
nlcc_rg = compute_rg_nlcc(pdb_file)

print("My result:", my_rg)
print("nlcc result", nlcc_rg)

result = True if np.all( my_dipole == nl_dipole ) else False

