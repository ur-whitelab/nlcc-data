import os
t = md.load(os.path.join(_FILE_DIR_, 'e22g.pdb'))
top = t.topology
hp_res_list = ['ALA', 'VAL', 'LEU', 'ILE', 'PRO', 'PHE', 'CYS']
hydrophobic_res = [res.index for res in top.residues if str(res)[
    :3] in hp_res_list]
print(hydrophobic_res)
result = True if get_hydrophobic_residues(os.path.join(
    _FILE_DIR_, 'e22g.pdb')) == hydrophobic_res else False
