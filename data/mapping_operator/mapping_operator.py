import numpy as np
import MDAnalysis as mda

# read molecule
u = mda.Universe('water.gro')
molecule = u.atoms
# define atoms that belong to the a single bead
beads_mappings = [['OW', 'HW1', 'HW2']]
Mws_dict = dict(zip(molecule.names, molecule.masses))
M, N = len(beads_mappings), len(molecule)
CG_matrix = np.zeros((M, N))
index = 0
for s in range(M):
    for i, atom in enumerate(beads_mappings[s]):
        CG_matrix[s, i + index] = [v for k,
                                   v in Mws_dict.items() if atom in k][0]
    index += np.count_nonzero(CG_matrix[s])
    CG_matrix[s] = CG_matrix[s] / np.sum(CG_matrix[s])

result = True if np.isclose(
    CG_matrix, [0.88809326, 0.05595337, 0.05595337]).all() else False
