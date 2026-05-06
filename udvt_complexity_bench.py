import matplotlib.pyplot as plt
import numpy as np

def plot_complexity_collapse(n_max=50):
    n = np.arange(1, n_max)
    beta = 0.0038
    
    # Classical Exponential Time
    t_classical = 2**n
    # UDVT Polynomial Collapse
    t_udvt = n**(3 * (1 - beta))
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(n, t_classical, label='Classical (Exponential Time)', color='red')
    plt.semilogy(n, t_udvt, label='UDVT (Polynomial Collapse)', color='green', lw=2)
    
    plt.title("Computational Complexity: P vs NP via UDVT Vacuum Processing")
    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Operations (Log Scale)")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.show()

if __name__ == "__main__":
    plot_complexity_collapse()
  
