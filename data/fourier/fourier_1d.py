import numpy as np
from numpy.fft import fft

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

true_y = fft(x)

test_y = fourier_1d(x)

result = True if np.allclose(true_y, test_y) else False
