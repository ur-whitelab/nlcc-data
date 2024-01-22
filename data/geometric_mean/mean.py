import numpy as np

a = np.arange(1,11,1)
mean  = pow(np.prod(a), 1/len(a))

if np.isclose(mean, geometric_mean(a)) == True:
    result = True
else:
    result = False
