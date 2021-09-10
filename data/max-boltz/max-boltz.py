import numpy as np
import matplotlib.pyplot as plt

# input params
M = 32e-3           # for O2, kg/mol
R = 8.314           # J/mol.K
T = np.array([100, 200, 300, 400, 500, 600])

c_rms = np.sqrt(3.0*R*T/M)
print("rms speeds :", c_rms)

c_rms_codex = max_boltz_speed(T)
print("rms speeds from codex :", c_rms_codex)

# check
if np.all(abs(c_rms - c_rms_codex) <= 1e-2):
    result = True 
else:
    result = False


"""
plt.figure()
plt.grid()
plt.xlabel('Temperature (K)')
plt.ylabel('RMS speed (m/s)')
plt.plot(T, c_rms, 'o-', lw=2.0)
plt.show()
"""
