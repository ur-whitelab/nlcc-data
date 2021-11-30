from rdkit import Chem
smiles = 'CC1=CN=C(C(=C1OC)C)CS(=O)C2=NC3=C(N2)C=C(C=C3)OC'  # omeprazole
m = Chem.MolFromSmiles(smiles)
hbd = Chem.rdMolDescriptors.CalcNumHBD(m)
hba = Chem.rdMolDescriptors.CalcNumHBA(m)
wt = Chem.rdMolDescriptors.CalcExactMolWt(m)
logp = Chem.Crippen.MolLogP(m)

if hbd < 5 and hba < 10 and wt < 500 and logp < 5:
    passed = True
else:
    passed = False

result = True if lipinski_rule_of_five(smiles) == passed else False
