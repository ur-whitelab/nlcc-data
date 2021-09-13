import numpy as np

np.random.seed(0)
M = np.random.random((5,5))
r = np.linalg.matrix_rank(M)

result = True if np.isclose(r, rank(M)) else False