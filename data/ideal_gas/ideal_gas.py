# input
V = 20.0    # volume (in L)
n = 10.0    # in moles
R = 0.0821  # in L.atm/mol.K
T = 350     # in K 

P = n*R*T/V
print("Pressure =", P)

# check 
if np.isclose(P, ideal_gas_equ(n,R,T,V)) == True:
    result = True 
else:
    result = False
