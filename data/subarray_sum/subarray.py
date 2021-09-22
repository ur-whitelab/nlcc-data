import numpy as np

# A is an array of non-negative integers only 
A = np.array([28 ,1, 27, 6, 8, 14, 9, 19, 20, 7, 1, 5, 13, 10])
N = len(A)
S = 28

#print("A =", A)
#print("N =", N)
#print("S =", S)

def subarraySum(A, N, S):
    """
    continuous sub-array which adds to a given number S.
    """
    index = []
    for i in range(N):
        sum_ = A[i]
        if sum_ >= S:
            continue
        for j in range(i+1, N):
            sum_ += A[j]
            if sum_ == S:
                
                # 1-based indexing
                #index.append([i+1, j+1])
                
                # 0-based indexing
                index.append([i, j])
            elif sum_ > S:
                break
            else:
                continue
    return index if len(index) != 0 else np.array(-1)

data = subarraySum(A,N,S)
print(data)

# check
if np.all(data == subarray_sum(A,N,S)):
    result = True
else:
    result = False


