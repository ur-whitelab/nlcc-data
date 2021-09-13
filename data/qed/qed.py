from rdkit.Chem import QED
smiles = 'CC1=CN=C(C(=C1OC)C)CS(=O)C2=NC3=C(N2)C=C(C=C3)OC' # omeprazole
m = Chem.MolFromSmiles(smiles)
q = QED.qed(m)

result = True if np.isclose(qed(smiles), q) else False 