import numpy as np

x = np.array((0., 30., 45., 60., 90.))

true_y = np.tan(x)

pred_y = f_tan(x)

result = True if np.allclose(true_y, pred_y) else False