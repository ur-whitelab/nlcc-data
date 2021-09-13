import numpy as np

# input params
h = 6.626e-34 
v = 1.00e6
m = 9.11e-31

lam  = h/(m*v)
print("lam =", lam)

lam_codex = de_broglie(m,v)

# check 
if np.isclose(lam, lam_codex) ==  True:
    result = True
else:
    result = False





