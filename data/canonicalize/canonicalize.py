smiles = [
    'C1=CC=CN=C1',
    'c1cccnc1',
    'C([H])C'
]

ref_csmiles = [
    'c1ccncc1',
    'c1ccncc1',
    'CC'
]

csmiles = canonical(smiles)

print(csmiles)
print(ref_csmiles)

result = True
for r, c in zip(ref_csmiles, csmiles):
    result = result and r == c
