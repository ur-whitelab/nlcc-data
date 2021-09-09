import numpy as np

x_min = 1
x_max = 100

x = np.arange(x_min, x_max+1, dtype=int)
#print(x)

primes = []

for xi in x:
    c = 0
    for j in range(1, xi+1, 1):
        if xi % j == 0:
            c += 1
        if c > 2:
            break 
    if c == 2:
        primes.append(xi)
    else:
        pass

print("prime numbers :", primes)
#print("# of prime numbers :", len(primes))

primes_codex = prime_numbers(x_min, x_max)
print("prime numbers from codex :", primes_codex)

# check 
if np.all(primes == primes_codex):
    result = True
else:
    result = False

