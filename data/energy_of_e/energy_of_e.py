
import math
Rh = 2.18e-18
n = 3
energy_true = (-Rh/(n**2))
energy_nlcc = energy_of_e(n)

result = math.isclose(energy_true, energy_nlcc, rel_tol =1e-5)

