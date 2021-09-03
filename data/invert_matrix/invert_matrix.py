

import numpy as np

x = np.array([[1,-1], [2,6]])
m_i = invert_matrix(x)
x_i = np.array([[0.75,0.125], [-0.25,0.125]])

result = np.array_equal(m_i,x_i)




