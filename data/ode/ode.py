from scipy.integrate import solve_ivp
def exponential_decay(t, y): 
    return -0.5 * y
solution = solve_ivp(exponential_decay, [0, 10], [4], t_eval=[2,5,8])

result = True if np.allclose(solution, solve_ode(exponential_decay, [2,5,8], [4])) else False