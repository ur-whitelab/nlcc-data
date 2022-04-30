import numpy as np

prediction_level = 0.9
samples = range(1, 100)
p = 0.1
psum = 0
for n in samples:
    psum += (1 - p) ** (n - 1) * p
    if(psum >= prediction_level):
        break

result = True if num_trials(prediction_level, p) == n else False
