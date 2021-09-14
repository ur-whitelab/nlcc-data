import numpy as np

np.random.seed(0)
M = 100
predictions = np.random.normal(loc=10, scale=3, size=(M,))
targets = np.random.normal(loc=9, scale=2, size=(M,))

rmse = np.sqrt(((predictions - targets) ** 2).mean())
result = True if np.isclose(rmse, 3.61350) else False
