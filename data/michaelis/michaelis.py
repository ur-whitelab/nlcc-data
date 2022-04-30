import numpy as np

Vmax=10
K_M = 2
S = 1
v=Vmax*S/(S+K_M)

v_codex = reaction_velocity(Vmax, S, K_M)

# check 
if np.isclose(v, v_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
