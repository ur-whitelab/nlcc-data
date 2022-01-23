import numpy as np
import matplotlib.pyplot as plt

# input params 
L = 10     # length of the box
m = 1      # masss of the particle
n = 10     # quantum number 
hbar = 1      # planck constant

# energy
e_n = ((n**2)*(hbar**2)*(np.pi**2))/(2*m*L**2)
print("energy =", e_n)

e_n_codex = particle_in_box(n,m,L)  
print("energy from codex =", e_n_codex)


# check
if abs(e_n - e_n_codex) <= 1e-3:
    result = True 
else:
    result = False




