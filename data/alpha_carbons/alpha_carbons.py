import numpy as np
import os
import sys

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")

def alpha_carbons(pdb_file):
    import mdtraj as md
    pdb = md.load(pdb_file)
    cas = pdb.top.select("name CA")
    return cas

my_result = alpha_carbons(pdb_file)
nlcc_result = alpha_carbons_nlcc(pdb_file)

print("My result:", my_result)
print("nlcc result", nlcc_result)

result = True if np.all( my_result == nl_result ) else False
