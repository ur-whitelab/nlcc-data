import mdtraj as md
import os 
import random
#  _FILE_DIR_ = '.'
top_path = os.path.join(_FILE_DIR_,'top.pdb')
system = md.load_pdb(top_path)
h_bonds = md.baker_hubbard(system, periodic=False)
da_dist = md.compute_distances(system, h_bonds[:,[0,2]], periodic=False)
num = len(h_bonds)
# assert
hb_dist = hbdist(top_path)
idx_1 = random.randint(0,num)
check1 = abs(hb_dist[idx_1] - da_dist[idx_1])
idx_2 = random.randint(0,num)
check2 = abs(hb_dist[idx_2] - da_dist[idx_2])
tol = 0.01

result = True if check1 <= tol else False
