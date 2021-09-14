import numpy as np

def diag_assert(x):
    l, v = np.linalg.eig(x)
    d = np.diag(l)
    return v, d

x = np.array([6, -1, 2, 3]).reshape(2,2)
v, d = diag_assert(x)
v_i = np.linalg.inv(v)
test = np.round(v.dot(d).dot(v_i))
check1 = (test == x).all()
#print(check1)

n_v, n_d = diag(x)
n_v_i = np.linalg.inv(n_v)
res = np.round(n_v.dot(n_d).dot(n_v_i))
check2 = (res == x).all()

result = True if check1 == check2 else False
