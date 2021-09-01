from mdtraj import load_pdb
import os
t = load_pdb(os.path.join(_FILE_DIR_,'e22g.pdb'))
top = t.topology
hp_res_list = ['ALA', 'VAL', 'LEU', 'ILE', 'PRO', 'PHE', 'CYS']
hydrophobic_res = [res for res in top.residues if str(res)[:3] in hp_res_list]
result = True if get_hydrophobic_residues(os.path.join(_FILE_DIR_,'e22g.pdb')) == hydrophobic_res else False