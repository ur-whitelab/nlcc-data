import numpy as np

np.random.seed(0)
M = 100
a = np.random.normal(loc=10, scale=3, size=(M,M))
eig = np.linalg.eigvals(a)
s_r = np.amax(np.absolute(eig))

result = True if np.isclose(spectral_r(a), s_r) else False
