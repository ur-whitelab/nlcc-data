import numpy as np

# input params
r_out = 12  # outer radius (in cm) 
r_in = 10   # inner radius (in cm)
m = 100     # mass (in gm)

vol = (4/3)*np.pi*(r_out**3 - r_in**3)  # volume (in cm^3)
den = m/vol   # density (gm/cm^3)

#print("Volume =", vol, "cm^3")
print("Density =", den, "g/cm^3")

den_codex = den_sphere(r_in, r_out, m)
print("Density from codex =", den_codex, "g/cm^3")

# check
if abs(den - den_codex) <= 1e-3:
    result = True
else:
    result = False
