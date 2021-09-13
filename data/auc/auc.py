import numpy as np
from numpy import trapz

fx = np.array([5, 20, 4, 18, 19, 18, 7, 4])
dx = 5
auc = trapz(fx, dx=dx)

auc_codex = area_under(fx,dx)

if np.isclose(auc, auc_codex) == True:
    result = True
else:
    result = False
