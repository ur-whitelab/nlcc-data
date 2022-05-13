import numpy as np

wavelength = 0.05 #nm
d = 0.3 #nm
theta = np.arcsin(wavelength/(2*d))

theta_codex = bragg_angle(wavelength, d)
print(theta, theta_codex)

if np.isclose(theta, theta_codex) ==  True:
    result = True
else:
    result = False
