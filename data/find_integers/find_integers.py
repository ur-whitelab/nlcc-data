import numpy as np

int_set = find_integers(20,2,5)
if np.all(int_set == [0,10,20]):
    return True
else:
    return False
