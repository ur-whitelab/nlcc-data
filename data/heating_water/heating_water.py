import numpy as np

n = 2
T1 = 300
T2 = 350
C = 1*18./1000 #cal/g/deg
q = n*C*(T2-T1)
# heat in kilocalories

q_codex = heating_energy(n, T1, T2)

# check 
if np.isclose(q, q_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
