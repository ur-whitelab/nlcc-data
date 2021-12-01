import numpy as np
import pylab as plt
#def PE(q):
#    return (q**2-1.0)**2
#def F(q):
#    return -4.0 * q * (q**2-1.0)
def F(q,k=2):
    return -k*q

x_traj, v_traj = run_langevin_dynamics(0.1,-0.1,0.1,F,100000)
plt.plot(x_traj)
plt.show()
v_traj_half = np.array(v_traj)[len(v_traj)//2:]
msv = v_traj_half.var()
ideal_msv = 1 #kT/m

result = True if np.abs(msv-ideal_msv)/ideal_msv < 0.2 and np.abs(np.mean(x_traj[len(x_traj)//2:]))<0.1 else False
