import numpy as np
pressure = 0.02 #atm
temperature = 310 #K 
c = pressure/(0.08206*temperature)
result = True if np.abs(osmotic_pressure_concentration(pressure,temperature)-c)<0.01 else False
