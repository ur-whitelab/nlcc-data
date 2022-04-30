import numpy as np
import matplotlib.pyplot as plt

# input params
h = 6.634e-34       # J.s
c = 3.0e8           # m/s
k = 1.381e-23       # J.K-1
T = 5000            # in K 
lamb_val = 1.0e-6   # in m 


# spectral radiance
B = (2*h*c**2/lamb_val**5) * (1/(np.exp(h*c/(lamb_val*k*T)) - 1)) 
print("spectral radiance =", B)

B_codex = bb_radiation(lamb_val, T)
print("spectral radiance from codex =", B_codex)


# check 
if abs(B - B_codex) <= 1e-2:
    result = True
else:
    result = False


