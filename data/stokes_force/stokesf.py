import numpy as np

# inputs

pi = 3.142
eta= 0.83 #in Ns/m**2
v = 1.2e5 # in m/s 
r = 5e-3  # in m 

# Stokes' viscous force 

F = 6*pi*eta*r*v
print("Viscous force from Stokes'law:", F)

F_codex = stokes_f(eta,r,v)
print("Viscous force from codex:", F_codex)

# check 

if abs(F - F_codex) <= 1e-5:
    result = True
else:
    result = False


