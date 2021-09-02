import os
import mdtraj as md
import numpy as np
pdb_file = os.path.join(_FILE_DIR_,"1l2y.pdb")
pdb = md.load_pdb(pdb_file)
top = pdb.topology
CAs = [atom.index for atom in top.atoms if atom.name == 'CA']
atom_pairs = np.array[ [CAs[0],CAs[-1]] ]#.reshape(-1,2)

distance = md.compute_distances(pdb,atom_pairs)[0][0]
distance_prompt = get_distance(pdb_file)
diff = abs(distance_prompt - distance)
result = True if diff <= 0.01 else False
