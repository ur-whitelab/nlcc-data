import numpy as np
import matplotlib.pyplot as plt

# initial values
x0 = -2.0
v0 = 3.0

# parameters
dt = 0.0001
n_steps = 500000
m = 10.0

def cal_ene(x, v, m):
    """
    It calculates energies.
    """
    # using a double well potential
    pe = (x**2 - 4.0)**2
    ke  = 0.5*m*(v**2)
    te = pe+ke
    return pe,ke,te

def cal_force(x):
    """
    It calculates the force.
    """
    f = -2*(x**2 - 4)*(2*x)
    return f 

def pos_update(x,v,dt,f,m):
    """
    It updates the position of a particle.
    """
    x_n = x + (dt*v) + (0.5*(dt**2)*(f/m))
    return x_n

def vel_update(v,dt,f0,f1,m):
    """
    It updates the velocity of a particle.
    """
    v_n = v + (0.5*dt/m)*(f0+f1)
    return v_n

x_data = [x0]
v_data = [v0]
f_data = [cal_force(x0)]
pe_data = [cal_ene(x0,v0,m)[0]]
ke_data = [cal_ene(x0,v0,m)[1]]
te_data = [cal_ene(x0,v0,m)[2]]

out_data = [[x0,v0]]

#f_o = open('colvar', 'w')
#f_o.write("FIELDS! step pos vel force pote kine tote\n")
#f_o.write("      ".join([str(0), str(x_data[0]), str(v_data[0]), str(f_data[0]), str(pe_data[0]), str(ke_data[0]), str(te_data[0])])+"\n")

for i in range(1, n_steps+1, 1):
    
    #updating position
    xi = pos_update(x_data[i-1], v_data[i-1], dt, f_data[i-1], m)
    x_data.append(xi)

    # updating force
    fi = cal_force(xi)
    f_data.append(fi)

    # updating velocity
    vi = vel_update(v_data[i-1], dt, f_data[i-1], fi, m)
    v_data.append(vi)

    out_data.append([xi,vi])

    #updating energy
    pe_i, ke_i, te_i = cal_ene(xi, vi, m)
    pe_data.append(pe_i)
    ke_data.append(ke_i)
    te_data.append(te_i)

    # write to file
    #f_o.write("      ".join([str(i), str(x_data[i]), str(v_data[i]), str(f_data[i]), str(pe_data[i]), str(ke_data[i]), str(te_data[i])])+"\n")


out_data = np.array(out_data)
print("shape of out_data=", out_data.shape)
#print(out_data)

"""
plt.figure()
plt.grid()
plt.xlabel("x")
plt.ylabel("Potential Energy ")
plt.plot(x_data, pe_data, 'o-')
plt.show()
"""
# calculate the average position
avg_pos = np.average(x_data)
print("avg_pos =", avg_pos)

codex_data = vel_verlet(x0, v0, n_steps, m, cal_force(x), dt)
print("shape of codex_data =", codex_data.shape)

avg_pos_codex = np.mean(codex_data[:,0])
print("avg_pos_codex =", avg_pos_codex) 

# check the result
if abs(avg_pos - avg_pos_codex) < 1e-3:
    result = True
else:
    result = False

"""
if np.all(abs(out_data - codex_data) < 1e-3):
    result = True
else:
    result = False
"""



