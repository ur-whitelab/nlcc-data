# Importing Libraries 
import numpy as np

print("*******START OF CODE*******")
set_1 = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#set_1 = [0,1,2,3,2,3,5,6,8,9] 

a = np.array(set_1)
print("Given sequence =", a)

# making a copy of the given integer list
p_a = a.copy()

len_a = len(a)
#print(len_a)

count = 0

if len_a % 2 == 0:   # even number of integers in array
    print("Even number of integers in the list, %d" %len_a)
    d = int(len_a/2)

    # set 1 
    s_1 = a[: d :]
    print("s_1 =", s_1)
    
    # set 2 
    s_2 = a[: d-1 :-1]
    print("s_2 =", s_2)

    for i in range(d):
        if s_1[i] != s_2[i]:
            p_a[i] = s_2[i]
            count += 1
        else:
            pass
else:                # odd number of integers in array

    print("Odd number of integers in the list, %d" %len_a)
    d = int(len_a/2)
    print("integer at the center of the sequence =", a[d])

    # set 1 
    s_1 = a[: d :]
    print("s_1 =", s_1)

    # set 2
    s_2 = a[: d :-1]
    print("s_2 =", s_2)

    for i in range(d):
        if s_1[i] != s_2[i]:
            p_a[i] = s_2[i]
            count += 1
        else:
            pass

# Make sure that the CODE worked perfectly
for i in range(d):
    #print(p_a[i], p_a[len_a-(i+1)])
    if p_a[i] != p_a[len_a-(i+1)]:
        raise("ERROR: NOT A PALINDROMIC SEQUENCE")

print("Palindromic sequence =", p_a)
print("Number of changes made =", count)
print("********END OF CODE*********")


# checking if the function generated by nlcc gives the same result
if count == minimum_changes(a):
    result = True
else:
    result = False





