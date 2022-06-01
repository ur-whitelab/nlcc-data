import numpy as np
import sys

start = 300
N = 40
end = 400

def list_generator(start,N,end):
    list=[]
    for i in range(0,N):
        T_k=np.round( start + (end-start) * (1 - np.exp( float(i)/(N-1) )**1)/(1- np.exp(1)),2)
        list.append(T_k)
    return np.array(list)

my_list = list_generator(start,N,end)
nlcc_list = list_generator_nlcc()

print("My result:", my_list)
print("nlcc result", nlcc_list)

result = True if np.all( my_list == nl_list ) else False

