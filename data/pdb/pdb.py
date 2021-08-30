from mdtraj import load_pdb
t = load_pdb('G5.pdb')
result = True if load_from_pdb('G5.pdb').n_atoms == t.n_atoms else False