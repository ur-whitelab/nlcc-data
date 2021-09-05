n = 5

factorial = 1
for i in range(n, 1, -1):
    factorial *= i

print(factorial)

if factorial == cal_factorial(n):
    result = True
else:
    result = False



