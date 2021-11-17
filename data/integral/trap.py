import numpy

def f(x):
    return x ** 4 * np.log(x + np.sqrt(x ** 2 + 1))

a = 0
b = 5
n = 100

x = np.linspace(a,b,num=n)
test_intgr = np.trapz(f(x), x=x)

result = True if np.isclose(trap(f,n,a,b),test_intgr) else False
