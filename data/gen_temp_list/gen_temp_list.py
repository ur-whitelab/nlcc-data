import numpy as np
import sys

T_min = float(sys.argv[1])
N_temp = int(sys.argv[2])
T_max = float(sys.argv[3])

def temp_generator(T_min,N_temp,T_max,power=1):
    templist=[]
    for i in range(0,N_temp):
        T_k=np.round( T_min + (T_max-T_min) * (1 - exp( float(i)/(N_temp-1) )**power)/(1- exp(power)),2)
        templist.append(T_k)
    return np.array(templist)

my_templist = temp_generator(T_min,N_temp,T_max)
nlcc_templist = temp_generator_nlcc(T_min,N_temp,T_max)

print("My result:", my_templist)
print("nlcc result", nlcc_templist)

result = True if np.all( my_templist == nl_templist ) else False

