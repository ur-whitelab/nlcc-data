import mdtraj as md
import os 
#_FILE_DIR_='./'
traj_path = os.path.join(_FILE_DIR_,'com.dcd') 
top_path = os.path.join(_FILE_DIR_,'com.pdb')
traj = md.load(traj_path, top=top_path)
com_assert = md.compute_center_of_mass(traj)

#  assert

res = com(traj_path, top_path)

a = com_assert[0]
at = res[0]
b = com_assert[-1]
bt = res[-1]

c_1 = (a == at).all())
c_2 = (b == bt).all())

result = True if c_1 and c_2 else False
