smiles = 'C1([O-])C=CC=C1NCC[NH+]'
mol = Chem.MolFromSmiles(smiles)
sc = rdkit.Chem.rdMolHash.MolHash(
    mol, rdkit.Chem.rdMolHash.HashFunction.MurckoScaffold)
result = scaffold(smiles) == sc
