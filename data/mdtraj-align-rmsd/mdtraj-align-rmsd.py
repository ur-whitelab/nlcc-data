# importing libraries
import numpy as np
import mdtraj as md 


# load two structures
apo = md.load_pdb('vinculin2-apo-protein.pdb')
apo_top = md.load_pdb('vinculin2-apo-protein.pdb').topology

holo = md.load_pdb('vinculin2-holo-protein.pdb')
holo_top = md.load_pdb('vinculin2-holo-protein.pdb').topology

# alpha carbons
alphas_apo = [atom.index for atom in apo_top.atoms if atom.name == 'CA'][31::]
alphas_holo = [atom.index for atom in holo_top.atoms if atom.name == 'CA'][:-2:]


# align two structures
holo_aligned = holo.superpose(apo, 0, atom_indices=alphas_holo, ref_atom_indices=alphas_apo)

# measure rmsd
rmsd =  md.rmsd(holo_aligned, apo, 0, atom_indices=alphas_holo, ref_atom_indices=alphas_apo)[0]
print("RMSD =",rmsd, "nm")


rmsd_codex = align_rmsd(holo, apo, alphas_holo, alphas_apo) 
print("RMSD from CODEX =", rmsd_codex, "nm")


# check
if abs(rmsd - rmsd_codex[0]) <= 1e-2:
    result = True
else:
    result = False


