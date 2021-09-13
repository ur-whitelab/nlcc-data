import numpy as np

def discretize(location, grid):
    return tuple(int(np.digitize(l, g)) for l, g in zip(location, grid))

grid = [np.array([1,2,3,4]),np.array([1,2,3,4])]
location =[2.5,1.2]

bin_value = discretize(location,grid)

result = True if bin_value == discretize_fn(location,grid) else False 
