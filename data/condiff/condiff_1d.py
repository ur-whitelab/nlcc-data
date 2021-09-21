import numpy as np

x = np.array([1, 2, 4, 7, 0])

true_y = np.ediff1d(x)

pred_y = condiff_1d(x)

result = True if np.allclose(true_y,pred_y) else False
