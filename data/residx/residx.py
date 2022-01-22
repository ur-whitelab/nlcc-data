import mdtraj as md
import os

_FILE_DIR_ = '.'
pdb_path = os.path.join(_FILE_DIR_,'top.pdb')
system = md.load_pdb(pdb_path)
top = system.topology
lig_str = 'TMP'
idxs_assert = top.select(F"resname == {lig_str}")

# assert
idxs = residxs(pdb_path,lig_str)
result = True if (idxs == idxs_assert).all() else False
