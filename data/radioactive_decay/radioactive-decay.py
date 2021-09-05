# import libraries
import numpy as np
import matplotlib.pyplot as plt


# input params
c0 = 10000
t_half = 17.4   # in years 
t = 20.0        # in years 

def cal_ct(c0, t_half, t):
    """
    It calculates, ct = amount of radioactive element remaining after time t and decay constant k.
    NOTE: t_hlaf and t should be given in same unit.

    INPUT:
    ------
    c0 = initial amount of radioactive element present
    t_half = half_life of the radioactive element
    t = arbitary time

    OUTPUT: k, ct, c0_ct
    ------
    c0_ct = amount of radioactive element decayed in time t since beginning
    
    """
    k = np.log(2)/t_half

    ct = c0*np.exp(-k*t)

    c0_ct = c0 - ct

    return k, ct, c0_ct


rate_const, c_t, c0_ct = cal_ct(c0, t_half, t)
print("c(t) =", c_t)

c_t_codex = radioactive(c0, t_half, t)
print("c(t) obtained from codex =", c_t_codex)


# check 
if abs(c_t - c_t_codex) <= 1e-2:
    result = True 
else:
    result = False
