import numpy as np
N = 100

x = np.random.randn(N, 3)
beta = np.array([-1.5, 2, -0.5])
y = x @ beta + np.random.randn(N) * 0.01
w = np.random.randn(N) ** 2
w /= np.sum(w)

diag_w = np.zeros((N, N))
np.fill_diagonal(diag_w, w)
# remove bias
y -= np.mean(y)
# compute least squares fit
xtinv = np.linalg.pinv(
    x.T @ diag_w @ x
)
beta_hat = xtinv @ x.T @ (y * w)

beta_hat_m = lsq(x, y, w)

result = np.allclose(beta_hat, beta_hat_m)
