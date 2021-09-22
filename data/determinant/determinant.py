import numpy as np

np.random.seed(0)
M = 10
a = np.random.randn(M, M)
test_determinant = np.linalg.det(a)

result = True if np.isclose(
    determinant(a), test_determinant) else False
