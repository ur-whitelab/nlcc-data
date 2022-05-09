import numpy as np

A = 1
B = 2
C = 1
phi = np.pi/7

J = A+B*np.cos(phi)+C*np.cos(2*phi)

J_codex = coupling(phi,A,B,C)

if np.isclose(J, J_codex) ==  True:
    result = True
else:
    result = False
