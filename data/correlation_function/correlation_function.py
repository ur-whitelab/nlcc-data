# importing libraries 
import numpy as np
import os
import matplotlib.pyplot as plt

# load data
v = np.loadtxt(os.path.join(_FILE_DIR_, "colvar"), usecols=2, unpack=True)
#print(v1.shape)

def correl_fun(a,b):
    """
    It calculates the time dependent correlation function using single trajectory.

    FORMULA:
    -------
    C_{AB}(n\delta t) =  \frac{1}{M-n} sum_{m=1}^{M-n} a(x_{m\delta t}) b(x_{(m+n)\delta t}),    n=0,\dots,K,  K << M
    
    INPUTS:
    ------
    a,b = data set for two observables A and B which are function of phase space coordinates

    """

    M  = len(a)
    K = int(M/10)

    #print("M =", M)
    #print("K =", K)

    c_ab = []

    for n in range(K):
        #print("n =", n)
        val = 0
        for m in range(1, M-n):
            val += (a[m]*b[m+n])
        val /= (M-n)
        c_ab.append(val)

    return np.array(c_ab)/c_ab[0]


c_vv = correl_fun(v,v)
c_vv_nlcc = cal_correl_fun(v,v)


# check
if np.all(abs(c_vv - c_vv_nlcc) <= 1e-3) == True:
    result = True
else:
    result = False


"""
def plot(data, x_l, y_l, t):
    plt.figure()
    plt.grid()
    plt.xlabel(x_l, fontsize="12")
    plt.ylabel(y_l, fontsize="12")
    plt.title(t, fontsize=15)
    plt.plot(data, 'r.-')
    plt.show()

plot(c_vv, "n steps", "$C_{vv}$", "ACF $(C_{vv})$ vs. Time")
"""


