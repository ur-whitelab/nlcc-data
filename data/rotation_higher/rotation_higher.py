import numpy as np

B = 2
J = 3
D = 2

E_rot = B*J*(J+1) - D*(J**2)*((J+1)**2)

E_rot_codex = e_rot(B,J,D)

if np.isclose(E_rot, E_rot_codex) ==  True:
    result = True
else:
    result = False
