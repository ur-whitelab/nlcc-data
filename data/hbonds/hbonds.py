import mdtraj as md
import os 
#  _FILE_DIR_ = '.'
top_path = os.path.join(_FILE_DIR_,'top.pdb')
system = md.load_pdb(top_path)
h_bonds = md.baker_hubbard(system, periodic=False)
num = len(h_bonds)

result = True if hbonds(top_path) == num else False
