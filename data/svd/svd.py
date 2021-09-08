import numpy as np

# making a random 2D matrix (complex)
a = np.random.randn(5, 7) + 1j*np.random.randn(5, 7)

# singular value decomposition
u, s, v = svd_f(a)

a_1 = np.matmul(np.matmul(u, np.diag(s)), v[:5,:])

# check
if np.allclose(a, a_1) == True:
    result = True
else:
    result = False


