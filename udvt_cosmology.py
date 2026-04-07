UDVT v2.0 - Cosmological Background Solver
Solves the modified Friedmann equation and scalar field evolution.
"""

import numpy as np
from scipy.integrate import solve_ivp

def udvt_evolution(N, state, beta, Omega_m, Omega_vac, kappa=1e-60):
    """
    ODE system for UDVT background in e-folding time N = ln a.
    
    Parameters:
    N : float - e-folding time
    state : [phi, dphi_dN] - scalar field and its derivative
    beta : float - vacuum stiffness index
    Omega_m : float - matter density parameter today
    Omega_vac : float - vacuum density parameter today
    kappa : float - NMDC coupling constant
    
    Returns:
    [dphi_dN, d2phi_dN2]
    """
    phi, dphi_dN = state
    a = np.exp(N)
    H_sq = Omega_m * a**-3 + Omega_vac * a**(-2*beta)
    H = np.sqrt(H_sq)
    
    # Modified Klein-Gordon equation in e-folding time
    term_nmdc = 3 * kappa * H**2 * (dphi_dN**2)
    d2phi_dN2 = -3 * dphi_dN - (2 * beta * Omega_vac * a**(-2*beta)) / (H_sq * (1 + term_nmdc))
    
    return [dphi_dN, d2phi_dN2]

# Example usage
if __name__ == "__main__":
    # UDVT best-fit parameters
    params = {
        'beta': 0.0038,
        'Omega_m': 0.308,
        'Omega_vac': 0.692,
        'kappa': 1e-60
    }
    initial_state = [0.1, -0.0038]  # phi, dphi_dN
    
    N_span = (0.0, 10.0)  # from a=1 to a=exp(10) ~ 22026
    sol = solve_ivp(udvt_evolution, N_span, initial_state, args=(params['beta'], params['Omega_m'], params['Omega_vac'], params['kappa']), dense_output=True)
    
    print("Background evolution solved. Final scale factor: a =", np.exp(sol.t[-1]))
    print("Final Hubble parameter squared:", params['Omega_m']*np.exp(-3*sol.t[-1]) + params['Omega_vac']*np.exp(-2*params['beta']*sol.t[-1]))
