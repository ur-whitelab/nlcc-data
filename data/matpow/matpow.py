import numpy as np


x = np.array([[0, 1], [-1, 0]])

true_y = np.linalg.matrix_power(x,3)

pred_y = matpow(x,3)

result = True if np.allclose(true_y,pred_y) else False
