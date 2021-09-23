import numpy as np
# Taken from rdkit Docs
from rdkit import RDConfig, Chem
from rdkit.Chem import rdSubstructLibrary
library = rdSubstructLibrary.SubstructLibrary()
for mol in Chem.SDMolSupplier(os.path.join(RDConfig.RDDataDir, 
                              'NCI', 'first_200.props.sdf')):
    idx = library.AddMol(mol)
smiles = 'CCCCOC'
core = Chem.MolFromSmiles(smiles)
indices = library.GetMatches(core)

result = True if np.isclose(substructure(smiles, library), len(indices)) else False