import numpy as np

n_min = 400
n_max = 500
num = np.arange(n_min, n_max+1, 1)

n_list = []

def func_sum(n):
    """
    It returns the sum of digits in an integer.
    """
    sum1 = 0
    while n != 0:
        rem = n % 10
        sum1 += rem 
        n = n // 10
    return sum1

for n in num:
    if func_sum(n) % 2 == 0:
        n_list.append(n)
    else:
        pass

n_codex = sum_d(n_min, n_max)


# check 
if np.all(n_list == n_codex):
    result = True 
else:
    result = False
