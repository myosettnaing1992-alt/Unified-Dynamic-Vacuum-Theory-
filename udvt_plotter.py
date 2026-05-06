import matplotlib.pyplot as plt
import numpy as np
from udvt_cosmology import CosmologySolver

def plot_hubble_tension_resolution():
    z = np.linspace(0, 3, 100)
    solver = CosmologySolver(beta=0.0038)
    
    # UDVT Prediction
    h_udvt = [solver.hubble_parameter(zi) for zi in z]
    # Standard LCDM (Approximated)
    h_lcdm = 70 * np.sqrt(0.3 * (1+z)**3 + 0.7)
    
    plt.figure(figsize=(10, 6))
    plt.plot(z, h_udvt, label='UDVT Prediction (Resolved)', color='purple', lw=2)
    plt.plot(z, h_lcdm, '--', label='Standard LCDM', color='gray')
    
    plt.title("Hubble Parameter Evolution: UDVT vs LCDM")
    plt.xlabel("Redshift (z)")
    plt.ylabel("H(z) [km/s/Mpc]")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_hubble_tension_resolution()
  
