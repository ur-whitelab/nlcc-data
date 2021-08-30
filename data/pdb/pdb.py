from mdtraj import load_pdb
import os
t = load_pdb(os.path.join(_FILE_DIR_,'G5.pdb'))
result = True if load_from_pdb(os.path.join(_FILE_DIR_,'G5.pdb')).n_atoms == t.n_atoms else False