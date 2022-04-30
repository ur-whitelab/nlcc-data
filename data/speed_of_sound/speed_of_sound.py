import numpy as np

M=28
T=300
R=8.314
gamma=7/5
s = np.sqrt(gamma*R*T/(M/1000))

s_codex = speed_of_sound(T,M,gamma)

# check 
if np.isclose(s, s_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
