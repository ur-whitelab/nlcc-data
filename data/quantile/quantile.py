import numpy as np

np.random.seed(0)
M = 100
data = np.random.randint(1,M, size=(M,))
quantiles = [0.1, 0.5, 0.9]

result = True if np.isclose(
    quantile(data, quantiles), np.quantile(data, q=quantiles)) else False
