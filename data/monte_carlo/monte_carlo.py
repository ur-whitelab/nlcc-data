# importing libraries
import numpy as np

# functions
def pote(x):
    u = (x**2 - 4.0)**2
    return u

# input params 
x0 = -2.0
n_steps = 1000000
delta = 0.5
beta = 0.1

x_data = [x0]
pote_data = [pote(x0)]

for i in range(1, n_steps+1, 1):
    r = np.random.random()
    x_n = x_data[i-1] + delta*(r-0.5)
    p_acc = min([1, np.exp(-beta*(pote(x_n) - pote(x_data[i-1])))])
    if r < p_acc:
        x_data.append(x_n)
        pote_data.append(pote(x_n))
    else:
        x_data.append(x_data[i-1])
        pote_data.append(pote_data[i-1])

avg_x = np.mean(x_data, axis=0)
avg_x_codex = np.mean(monte_carlo_sampling(x0, n_steps, pote(x)), axis=0)

# check
if abs(avg_x - avg_x_codex) <= 1e-2:
    result = True
else:
    result = False




