import numpy as np

# make a data set 
a = np.exp(2j * np.pi * np.arange(10) / 10)

# 1D fourier transform by codex
f_a = fourier_transform(a)

# inverse fourier transformation
gen_a = np.fft.ifft(f_a)

# check
if np.allclose(a, gen_a) == True:
    result = True
else:
    result = False

