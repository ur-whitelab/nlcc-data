import numpy as np

n_rows = 13
num = np.arange(1, np.sum(np.arange(1, n_rows+1, 1))+1, 1)

print("Output: script\n--------------")
c = 0
for i in range(1, n_rows+1):
    num_o = " ".join([str(num[j]) for j in range(c, c+i,1)])
    c += i
    print(num_o)



print("Output: CODEX\n--------------")
floyd_triangle(n_rows)


# check 
result = True if floyd_triangle(n_rows) != None else False
