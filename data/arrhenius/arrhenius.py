import numpy as np

# inputs
T1 = 308.18   # in K
T2 = 333.18   # in K
R = 8.314     # J/mol.K
Ea = 108000   # J/mol
k2 = 1e-3     # M-1 s-1 

k1 = k2*np.exp((-Ea/R) * (1/T1 - 1/T2))
k1_codex = arrhenius(k2,T2,T1,Ea)
#print(k1,k1_codex)

if np.isclose(k1,k1_codex) == True:
    result = True
else:
    result = False

