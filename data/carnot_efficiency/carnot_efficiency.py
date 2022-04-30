import numpy as np

T_cold = 300
T_hot = 600

eps = 1 - T_cold/T_hot

eps_codex = carnot_efficiency(T_hot, T_cold)

# check 
if np.isclose(eps, eps_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
