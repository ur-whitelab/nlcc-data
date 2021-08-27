import numpy as np

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[10,11,12],[13,14,15],[16,17,18]]

c = np.matmul(a,b)

d = get_matmul(a,b)

result = True if c==d else false
