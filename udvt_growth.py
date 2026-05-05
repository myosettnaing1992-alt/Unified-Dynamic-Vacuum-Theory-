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
import numpy as np

def calculate_effective_g(k, B_phi, k_myo, G_N=6.67430e-11):
    """
    Calculates the scale-dependent effective gravitational constant (G_eff) 
    according to Unified Dynamic Vacuum Theory (UDVT) Chapter 4.
    
    Parameters:
    -----------
    k : float or ndarray
        Wavenumber in h/Mpc.
    B_phi : float
        The disformal coupling factor B(phi) at a given epoch.
        (Note: B(phi) > -1 to satisfy the Myo Limit).
    k_myo : float
        The characteristic scale of the Myo Limit (typically ~0.5 h/Mpc).
    G_N : float, optional
        Standard Newton's constant. Default is SI units.

    Returns:
    --------
    G_eff : float or ndarray
        The modified gravitational constant at scale k.
    """
    
    # Validation for the Myo Limit safety margin
    if np.any(B_phi <= -1):
        raise ValueError("Myo Limit Violation: B(phi) must be greater than -1.")

    # Term 1: Background modification due to disformal coupling
    background_mod = G_N / (1 + B_phi)
    
    # Term 2: Scale-dependent suppression factor (The Myo Factor)
    # As k increases (smaller scales), gravity is suppressed.
    suppression_factor = 1 / (1 + (k / k_myo)**2)
    
    effective_g = background_mod * suppression_factor
    
    return effective_g

# Example Usage:
# k_vals = np.array([0.01, 0.1, 0.5, 1.0, 10.0]) # h/Mpc
# g_vals = calculate_effective_g(k_vals, B_phi=0.0038, k_myo=0.5)def get_G_eff(k, a, B_phi, k_myo):
    G_N = 6.67430e-11
    # From Chapter 4: G_eff(k,t) = G_N / (1+B) * 1 / (1 + k^2/k_myo^2)
    return (G_N / (1 + B_phi)) * (1 / (1 + (k/k_myo)**2))
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
def growth_ode(a, y, B_phi, k_myo, Omega_m0):
    """
    Defines the ODE for the linear growth factor D(a) in UDVT.
    y[0] = D (growth factor)
    y[1] = dD/da
    """
    D, dD_da = y
    
    # Calculate G_eff/G_N modification for a specific k-scale
    # Note: k is usually fixed here to see the scale-dependent growth
    k_test = 0.1 # h/Mpc example
    g_ratio = calculate_effective_g(k_test, B_phi, k_myo) / 6.67430e-11
    
    # Modified Growth Equation (simplified version)
    # d^2D/da^2 + (3/a + dH/da / H) dD/da - 1.5 * Omega_m(a)/a^2 * (G_eff/G_N) * D = 0
    # This g_ratio directly drives the suppression of σ8
    
    term1 = -(3/a) * dD_da # Assuming LCDM-like expansion for friction term
    term2 = 1.5 * (Omega_m0 / a**3) * g_ratio * D
    
    return [dD_da, term1 + term2]
    
