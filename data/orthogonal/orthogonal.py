import numpy as np
import matplotlib.pyplot as plt

"""
# input params
na = 6.023e23
c = 3.0e8
m = 8e-3
w = 2*np.pi*1580.0*1e2*c
print("w =", w)
h_bar = (6.634e-34/(2*np.pi))*na   # J.s/mol
print("h_bar =", h_bar)
"""
m = 1
w = 1
h_bar = 1 
alpha = (m*w/h_bar)


# Quantum Harmonic Oscillator wave functions
x = np.linspace(-5, 5, 100, endpoint=True)
y0 = (alpha/np.pi)**(1/4) * np.exp(-alpha*x**2/2.0) 
y1 = (alpha/np.pi)**(1/4) * np.exp(-alpha*x**2/2.0) * np.sqrt(2*alpha)*x
y2 = (alpha/np.pi)**(1/4) * np.exp(-alpha*x**2/2.0) * ((2*alpha*x**2 -1)/np.sqrt(2))
y3  = (alpha/np.pi)**(1/4) * np.exp(-alpha*x**2/2.0) * (2*alpha**1.5*x**3 -3*np.sqrt(alpha)*x) * (1/np.sqrt(3))


# calcualte the overlap integral
d = np.trapz(y0*y2, x, axis=0) 

if orthogonal(y0,y1) == np.isclose(d, 0.0):
    result = True
else:
    result = False


"""
# plot
plt.figure()
plt.grid()
plt.xlabel('x', fontsize=12)
plt.ylabel('$\psi_{n}(x)$', fontsize=12)
plt.title('Quantum Harmonic Oscillator: Wave Functions', fontsize=12)
plt.plot(x, y0, '-', label='$\psi_0(x)$', lw=2.0)
plt.plot(x, y1, '-', label='$\psi_1(x)$', lw=2.0)
plt.plot(x, y2, '-', label='$\psi_2(x)$', lw=2.0)
plt.plot(x, y3, '-', label='$\psi_3(x)$', lw=2.0)
plt.plot(x, y0*y2, '-', label='$\psi_0(x)\psi_2(x)$', lw=2.0)

plt.legend()
plt.show()
"""
