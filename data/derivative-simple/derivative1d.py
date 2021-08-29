import numpy as np

fx = np.poly1d([1, 2, 3])
fprime = fx.deriv()
result = True if fprime(2) == 6 else False
