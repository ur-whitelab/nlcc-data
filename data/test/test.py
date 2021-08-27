import numpy as np
import mdtraj as md
import sys

pdb_file=sys.argv[1]

def compute_rg_mdtraj(pdb_file):
    pdb_file = md.load(pdb_file)
    return md.compute_rg(pdb_file, masses=None)

my_result=compute_rg_mdtraj(pdb_file)

nlcc_result=compute_rg(pdb_file)

result=True if my_result==nlcc_result else False

