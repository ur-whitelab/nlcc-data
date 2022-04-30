import numpy as np
P1 = 1
P2 = 2
T1 = 300
gamma = 5/3

T2 = T1*((P2/P1)**((gamma-1)/gamma))

T2_codex = cooling(T1, P1, P2, gamma)

# check 
if np.isclose(T2, T2_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
