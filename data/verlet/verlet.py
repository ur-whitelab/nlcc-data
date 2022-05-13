import numpy as np


def ref_verlet_integrate(x0, v0, F, steps=1000, dt=0.001):
    """
    This function runs velocity verlet integration with the given force function F.
    """
    x_traj = np.zeros(steps)
    v_traj = np.zeros(steps)
    x_traj[0] = x0
    v_traj[0] = v0
    for i in range(steps-1):
        v = v_traj[i] + 0.5 * F(x_traj[i]) * dt
        x_traj[i+1] = x_traj[i] + v * dt
        v_traj[i+1] = v + 0.5 * F(x_traj[i+1])*dt
    return x_traj, v_traj


def F(q, k=2):
    return -k*q


def U(q, k=2):
    return 0.5 * k*q**2


x_traj, v_traj = verlet_integrate(0.1, -0.1, F, 100000, dt=1e-3)
xr_traj, vr_traj = ref_verlet_integrate(0.1, -0.1, F, 100000, dt=1e-3)
result = np.allclose(x_traj, xr_traj) and np.allclose(v_traj, vr_traj)
