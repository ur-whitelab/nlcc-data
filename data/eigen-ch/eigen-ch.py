import numpy as np

np.random.seed(0)
M = np.random.random((5,5))
w, v = np.linalg.eig(M)
w1, v1 = eigen(M)
result = True if np.allclose(w, w1) and np.allclose(v,v1) else False