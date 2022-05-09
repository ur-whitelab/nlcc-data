import numpy as np

B = 2
J = 3

E_rot = B*J*(J+1)

E_rot_codex = e_rot(B,J)

if np.isclose(E_rot, E_rot_codex) ==  True:
    result = True
else:
    result = False
