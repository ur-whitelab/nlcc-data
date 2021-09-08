def fib_assert(n):
    phi = (1+5**0.5)/2
    psi = (1-5**0.5)/2
    a = (phi**n - psi**n)/(5**0.5)
    return round(a)

result = True if fib(20) == fib_assert(20) else False
