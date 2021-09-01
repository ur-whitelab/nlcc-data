import numpy as np
import sys
import os

pdb_file = os.path.join(_FILE_DIR_,"1VII.pdb")

def pair_wise(pdb_file):
    import mdtraj as md
    from itertools import combinations
    pdb = md.load(pdb_file)
    cas=pdb.top.select("name CA")
    distances = []
    comb = combinations(cas, 2)
    for p in comb:
        d=md.compute_distances(pdb,[[p[0],p[1]]], periodic=True)
        distances.append(d)
    return np.array(distances).flatten()

my_result = pair_wise(pdb_file)
nlcc_result = pair_wise_nlcc(pdb_file)

print("My result:", my_result)
print("nlcc result", nlcc_result)

result = True if np.all( my_result - nlcc_result )<0.1 else False
