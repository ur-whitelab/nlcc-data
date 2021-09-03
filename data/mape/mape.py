import numpy as np

np.random.seed(0)
M=100
y_hat = np.random.normal(loc=10,scale=3,size=(M,))
y = np.random.normal(loc=9, scale=2, size=(M,))

test_mape = abs((y - y_hat)*100/ y).mean()
result = True if mape(y_hat,y)==test_mape else False
