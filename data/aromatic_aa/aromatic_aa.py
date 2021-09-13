phenylalanine = "F"
leucine = "L"


result = True if aromatic_aa(phenylalanine)=="aromatic" and aromatic_aa(leucine) =="non-aromatic" and aromatic_aa("X") =="error" else False


