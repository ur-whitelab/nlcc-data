import numpy as np

# input params
M = 32e-3           # for O2, kg/mol
R = 8.314           # J/mol.K
T = 300

c_rms = np.sqrt(3.0*R*T/M)
#print("rms speeds :", c_rms)

M_in_kg = M/6.022e23

c_rms_codex = max_boltz_rms_speed(T,M_in_kg)
#print("rms speeds from codex :", c_rms_codex)

# check
if np.isclose(c_rms,c_rms_codex,rtol=0.01):
    result = True 
else:
    result = False
