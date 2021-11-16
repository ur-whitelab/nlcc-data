import numpy as np
import os
# Taken from rdkit Docs
from rdkit import RDConfig, Chem
from rdkit.Chem import rdSubstructLibrary
library = rdSubstructLibrary.SubstructLibrary()
llibrary = []
for mol in Chem.SDMolSupplier(os.path.join(RDConfig.RDDataDir,
                                           'NCI', 'first_200.props.sdf')):
    idx = library.AddMol(mol)
    llibrary.append(mol)
smiles = 'CCCCOC'
core = Chem.MolFromSmiles(smiles)
indices = library.GetMatches(core)

result = True if np.isclose(len(substructure(
    smiles, llibrary)), len(indices)) else False
