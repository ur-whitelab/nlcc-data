import numpy as np

# input
V = 20.0    # volume (in L)
n = 10.0    # in moles
R = 0.08206  # in L.atm/mol.K
T = 350     # in K 

P = n*R*T/V
#print("Pressure =", P)

codex_pressure = ideal_gas_pressure(n,V,T)
#print("Codex pressure =", codex_pressure)
# check 
if np.isclose(P, codex_pressure, rtol=0.01) == True:
    result = True 
else:
    result = False
