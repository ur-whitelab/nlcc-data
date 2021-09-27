import mdtraj as md
import os 
import random
#  _FILE_DIR_ = '.'
top_path = os.path.join(_FILE_DIR_,'top.pdb')
system = md.load_pdb(top_path)
h_bonds = md.baker_hubbard(system, periodic=False)
da_dist = md.compute_distances(system, h_bonds[:,[0,2]], periodic=False)
num = len(da_dist[0])
hb_dist = hbond_distance(top_path)

#compare shorted hbond length
check1 = abs(hb_dist[np.argsort(hb_dist)[0]] - da_dist[np.argsort(da_dist)[0]])
tol = 0.01
result = True if check1 <= tol else False
