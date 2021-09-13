import numpy as np

np.random.seed(0)
M = 100
targets = np.random.rand(M)
predictions = targets * 0.9
kle_loss = -np.sum(targets*np.log(
    np.divide(predictions, targets) + 1e-10))

result = True if np.isclose(kle(targets, predictions), kle_loss) else False
