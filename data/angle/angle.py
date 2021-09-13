import numpy as np

def unit_vec(vector):
    return vector / np.linalg.norm(vector)

v1 =  [1.2,0.5,0.5]
v2 =  [-1.5,2.0,0.0]

v1_u = unit_vec(v1)
v2_u = unit_vec(v2)

angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

angle_codex =  vector_angle(v1,v2)

if np.isclose(angle, angle_codex) == True:
    result = True
else:
    result = False
