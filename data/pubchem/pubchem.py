import requests
import time

time.sleep(0.5)


def ref_find_similar(s):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/smiles/{s}/property/CanonicalSMILES/JSON"
    reply = requests.get(
        url,
        params={"Threshold": 80, "MaxRecords": 100},
        headers={"accept": "text/json"},
        timeout=10,
    )
    data = reply.json()
    smiles = [d["CanonicalSMILES"]
              for d in data["PropertyTable"]["Properties"]]
    smiles = set(smiles)
    return smiles


s = 'CC=C=C(C(=O)N)'
ref_sim = ref_find_similar(s)
sim = find_similar(s)
result = True if ref_sim == set(sim) else False
