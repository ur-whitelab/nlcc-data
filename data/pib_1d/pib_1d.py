import numpy as np
import matplotlib.pyplot as plt

# input params 
L = 10     # length of the box
m = 1      # masss of the particle
n = 10     # quantum number 
h = 1      # planck constant

# energy
e_n = (n**2*h**2)/(8*m*L**2)
print("energy =", e_n)

# wave function
x  = np.linspace(0, L, 50, endpoint=True)
w_n = np.sqrt(2/L) * np.sin(n*np.pi*x/L)


e_n_codex = pib_energy(n,m,L,h)  
print("energy from codex =", e_n_codex)


# check
if abs(e_n - e_n_codex) <= 1e-3:
    result = True 
else:
    result = False




