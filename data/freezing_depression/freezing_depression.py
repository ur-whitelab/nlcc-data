import numpy as np
molality = 0.1
depression_constant = -0.512
dT = depression_constant*molality
result = True if np.abs(freezing_depression(depression_constant,molality)-dT)<0.01 else False
