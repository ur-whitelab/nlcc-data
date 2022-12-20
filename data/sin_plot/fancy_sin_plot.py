import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0)
y = np.sin(np.pi*x)**2
plt.plot(x, y, marker='^', markersize=10, linestyle='-.', linewidth=3,
            color='b', label=r'$\sin^2(\pi x)$')
plt.legend(loc='lower right')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('A basic plot')
plt.savefig('fancy_sin_plot.png')
