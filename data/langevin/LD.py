import numpy as np
def PE(q):
    return (q**2-1.0)**2
def F(q):
    return -4.0 * q * (q**2-1.0)

q_trj,p_trj = run_langevin_dynamics(1.0,0.0,1.0,1.0,2.0,PE,F,10000,dt=0.001,k_B=1.0)
p_trj = np.array(p_trj)[len(p_trj)//2:]
second_moment = np.mean(p_trj**2)
ideal = 1.0 * 1.0 * 2.0
result = True if np.abs(second_moment-ideal)/ideal < 0.1 else False
