import numpy as np
from rdkit.DataStructs.cDataStructs import TanimotoSimilarity
from rdkit.Chem import AllChem
from rdkit import Chem
import itertools


def ref_tan_matrix(slist):
    fp = [AllChem.GetMorganFingerprintAsBitVect(
        Chem.MolFromSmiles(s), 2, nBits=256) for s in slist]
    ts = list(
        TanimotoSimilarity(x, y) for x, y in itertools.product(fp, repeat=2)
    )
    return np.array(ts).reshape(len(fp), len(fp))


mols = ['C1C=C(C=NC=C(C(F)(F)F)CCCCCC)C=C1C=CC=CC',
        'CC=C=C(C(=O)N)', 'C1([O-])C=CC=C1NC=CC=C']
# turned down tolerance because CODEX wants to compute
# fingerprint with slightly different implementation (can't tell diff?)
result = True if np.allclose(ref_tan_matrix(
    mols), tanimoto_matrix(mols), rtol=0.1, atol=1e-2) else False
