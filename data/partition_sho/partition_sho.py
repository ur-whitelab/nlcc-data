# importing libraries
import numpy as np
import matplotlib.pyplot as plt


# input params
na = 6.023e23                               # avogradro's number 
stretch_freq = 4342.0                       # in cm-1  (this one is for H2)
c = 3.0e8                                   # speed of light(in m/s)
omega = 2*np.pi*c*stretch_freq*100          # unit (in s-1) 
k =  1.381e-23*na                           # boltzmann constant (j/mol.K)
T =  3000.0                                  # temperature in K 
h_bar = (6.634e-34*na)/(2*np.pi)            # J.s/mol
beta = 1.0/(k*T)                            # (J/mol)-1


#print("=============INPUT PARAMS=========")
#print("avogadro's number =", na, "/mol")
#print("vibrational stretching frequency =", stretch_freq, "cm-1")
#print("speed of light =", c, "m/s")
#print("omega =", omega, "s-1")
#print("boltzmann constant =", k, "J/mol.K")
#print("temperature =", T, "K")
#print("planck's constant =", h_bar, "J.s/mol")
#print("beta (1/kT) =", beta, "(J/mol)-1")
#print("=================================")


def q_sho(b, h, w):
    """
    It calculates the partition function for SHO.
    
    INPUT:
    ----
    b = beta (1/kT)
    h = h_bar (h/2*pi)
    w = omega

    OUTPUT:
    -----
    q = partition function for SHO

    """
    q = np.exp(-b*h*w/2)/(1 - np.exp(-b*h*w))

    return q

q = q_sho(beta, h_bar, omega)

print("partition function =", q)

# check 
q_codex = cal_partition(omega, T)
print("partition function (codex) =", q_codex)

if abs(q-q_codex) <= 0.01:
    result = True
else:
    result = False




"""
# make a plot of q vs. T
temp_data = np.linspace(300.0, 3000.0, 20, endpoint=True)
q_data = []
beta_data = []

for temp in temp_data:

    # calculate beta
    beta_temp = 1/(k*temp)
    beta_data.append(beta_temp)
    
    # calculate q 
    q_temp = q_sho(beta_temp, h_bar, omega)
    q_data.append(q_temp)

plt.figure()
#plt.plot(np.ones(len(beta_data))/beta_data, q_data, 'o-')
for i in range(len(temp_data)):
    plt.plot(temp_data[i], q_data[i], 'o', label="%d K"% temp_data[i])
plt.xlabel("Temperature (K)", fontsize=12)
plt.ylabel("Q", fontsize=12)
plt.title("Partition Function for SHO (1D)", fontsize=12)
plt.legend(ncol=3, loc="upper left", markerscale=0.2, fontsize=8.0)
plt.show()

"""






