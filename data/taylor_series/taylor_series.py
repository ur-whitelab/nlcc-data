import numpy as np
import math

def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += (coef) * ((num)/(denom))
    return cos_approx

x = math.radians(45)
n = 8

result = True if np.isclose(taylor_series(
    func_cos, x, n), func_cos(x,n)) else False
