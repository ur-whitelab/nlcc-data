import mdtraj as md
import numpy as np
pdb = md.load_pdb("1l2y.pdb")
top = pdb.topology
CAs = [atom.index for atom in top.atoms if atom.name == 'CA']
#atom_pairs = []
#atom_pair = [CAs[0],CAs[-1]]
#atom_pairs.append(atom_pair)
#atom_pairs = np.array(atom_pairs)
atoms_pairs = [[CAs[0],CAs[-1]]]
distance = md.compute_distances(pdb,atom_pairs)
distance_prompt = get_distance("1L2y.pdb")
diff = abs(distance_prompt - distance[0,0])
result = True if diff <= 0.01 else False
