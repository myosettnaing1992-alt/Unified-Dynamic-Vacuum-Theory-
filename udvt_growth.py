#UDVT v2.0 - Linear Growth Factor and sigma_8 Calculation
Computes the matter perturbation growth and the suppression of clustering.
"""

import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

def growth_factor_udvt(a_range, beta, Omega_m):
    """
    Calculate linear growth factor D(a) for UDVT.
    
    Parameters:
    a_range : array-like - scale factor values (must be increasing)
    beta : float - vacuum stiffness
    Omega_m : float - matter density today
    
    Returns:
    D : array - growth factor normalized to 1 at a=1
    """
    def growth_ode(y, ln_a):
        D, dD_dln_a = y
        a = np.exp(ln_a)
        # Scale-dependent G_eff (simplified model)
        G_eff_ratio = 1.0 + 2 * beta**2 / (1 + (a/0.01)**2)
        # Background expansion
        H_sq = Omega_m * a**-3 + (1 - Omega_m) * a**(-2*beta)
        H = np.sqrt(H_sq)
        f = -0.5 * (3*Omega_m*a**-3 + 2*beta*(1-Omega_m)*a**(-2*beta)) / H_sq
        d2D = -(2 + f) * dD_dln_a + 1.5 * G_eff_ratio * (Omega_m * a**-3 / H_sq) * D
        return [dD_dln_a, d2D]
    
    ln_a = np.log(a_range)
    # Initial conditions at early times (a=1e-4, matter-dominated)
    D0 = 1e-4
    dD0 = 1e-4  # approx D ~ a
    y0 = [D0, dD0]
    sol = odeint(growth_ode, y0, ln_a)
    D = sol[:, 0]
    # Normalize to 1 at a=1
    D /= np.interp(1.0, a_range, D)
    return D

def sigma8_udvt(beta, Omega_m, sigma8_lcdm=0.811):
    """
    Predict sigma_8 in UDVT from the growth suppression factor.
    
    Parameters:
    beta : float - vacuum stiffness
    Omega_m : float - matter density
    sigma8_lcdm : float - LambdaCDM sigma8 at z=0
    
    Returns:
    sigma8_udvt : float
    """
    # Approximate suppression factor from late-time growth modification
    suppression = 1.0 - 0.5 * beta
    return sigma8_lcdm * suppression

if __name__ == "__main__":
    beta = 0.0038
    Omega_m = 0.308
    a_arr = np.logspace(-4, 0, 100)
    D = growth_factor_udvt(a_arr, beta, Omega_m)
    sigma8_pred = sigma8_udvt(beta, Omega_m)
    print(f"UDVT sigma_8 prediction: {sigma8_pred:.4f} (observed: 0.750±0.015)")
