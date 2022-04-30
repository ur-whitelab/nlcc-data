import numpy as np

m=32
T=300
R=8.314
v_rms = np.sqrt(3*R*T/(m/1000))

v_rms_codex = rms_velocity(T,m)

# check 
if np.isclose(v_rms, v_rms_codex, rtol=0.01) == True:
    result = True 
else:
    result = False
