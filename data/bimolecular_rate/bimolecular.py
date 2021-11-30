import numpy as np

k = 2
A = 0.1
B = 0.2
rate = k*A*B

result = True if np.isclose(rate,bimolecular_rate(k,A,B)) else False

