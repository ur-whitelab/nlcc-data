n_rows = 7

data = []
print("output: script\n-------------")
for i in range(1,n_rows+1,1):
    a = [1]*i
    if i >= 3:
        for j in range(1,len(a)-1,1):
            a[j] = data[-1][j-1] + data[-1][j]
    data.append(a)
    print(" ".join(str(k) for k in a))


print("output: codex\n-------------")
pascal_triangle(n_rows)


# check
if pascal_triangle(n_rows) != None:
    result = True 
else:
    result = False
