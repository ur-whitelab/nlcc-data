import numpy as np

# input
hvap = 5000 #J/mol
P1 = 1 # atm
R = 8.314 # 8.314 J/k mol
T1 = 300     # in K 
T2 = 350 

P2_codex = claussius(hvap, T1, P1, T2)
P2 = P1*np.exp(-hvap/R*(1/T2-1/T1))

# check 
if np.isclose(P2, P2_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
