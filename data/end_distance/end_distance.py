import os
#import mdtraj as md
import numpy as np
pdb_file = os.path.join(_FILE_DIR_,"1l2y.pdb")
def compute_end_distance(pdb_file):
  import mdtraj as md
  pdb = md.load(pdb_file)
  top = pdb.topology
  CAs = [atom.index for atom in top.atoms if atom.name == 'CA']
  atom_pairs = np.array[ [CAs[0],CAs[-1]] ]#.reshape(-1,2)
  distance = md.compute_distances(pdb,atom_pairs)[0][0]
  return distance
my_distance = compute_end_distance(pdb_file)
prompt_distance = calculate_distance(pdb_file)

diff = abs(prompt_distance - my_distance)
result = True if diff <= 0.01 else False
