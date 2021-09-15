import numpy as np

# make sure the array contains only distinct positive integers
a = [3, 9, 10, 7, 18, 12, 17, 30, 8, 21, 2, 19]
n = len(a)

def countTriplet(arr, n):
    """
    This function returns the triplet count in a given array.
    """
    #print("Given array: ", arr)
    #print("number of elements =", n)
    
    # sorting 
    sort_arr = sorted(arr)
    #print("sorted array: ",sort_arr)
    
    count  = 0
    for i in range(2, n):
        num_i = sort_arr[i]
        for j in range(i):
            for k in range(j+1,i):
                if sort_arr[j] + sort_arr[k] == num_i:
                    #print(str(sort_arr[j])+" + "+str(sort_arr[k])+" = "+str(num_i))
                    count += 1
    return count

c = countTriplet(a,n)
#print("Triplet count =",c)
 
if c == count_triplets(a):
    result = True
else:
    result = False
