import numpy as np

np.random.seed(0)
M = 100
# (k-> inf)
k = 50
a = np.random.normal(loc=10, scale=3, size=(M,M))
matrix = np.linalg.matrix_power(a, k)
f_norm = np.linalg.norm(matrix, 'fro')
s_r = f_norm**(1.0/k)

result = True if np.isclose(spectral_r(a), s_r) else False
