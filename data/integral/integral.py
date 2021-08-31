import numpy as np

result = True if find_integral(1,2,3,4) == np.poly1d([1/4, 2/3, 3/2, 4]) else False 