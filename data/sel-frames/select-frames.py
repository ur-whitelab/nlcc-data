import os
import mdtraj as md 

traj = md.load(os.path.join(_FILE_DIR_,'trp-cage-small.trr'), top=os.path.join(_FILE_DIR_,'trp-cage.pdb'))
result = True if select-frames('trp-cage-small.trr','trp-cage.pdb',50).n_frames == traj[:50].n_frames else False
