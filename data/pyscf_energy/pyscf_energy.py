atom_coordinates = "H 0 0 0; F 0 0 1"
basis = "sto-3g"

#so that it doesn't fail b/c not importing these in prompt:
from pyscf import gto, scf

def calc_molecule_energy_test(atom_coordinates,basis):
    mol = gto.M(atom=atom_coordinates,basis=basis)
    mf = scf.RHF(mol)
    return mf.kernel()

my_energy = calc_molecule_energy_test(atom_coordinates,basis)
nlcc_energy = calc_molecule_energy(atom_coordinates,basis)

print("My result:", my_energy)
print("nlcc result:", nlcc_energy)

result = True if np.abs( my_energy - nlcc_energy )<0.1 else False
