
import numpy as np

x = np.array([[1, 2, 3], [4,5,6]])
m_f = matrix_factorial(x)
x_f = np.array([[1, 2, 6], [24,120,720]])

result = True if np.array_equal(x_f,m_f) else False