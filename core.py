import numpy as np
import matplotlib.pyplot as plt

class MyoConsistencyEngine:
    def __init__(self, beta=0.0038, h0_local=73.04, omega_m=0.315):
        self.beta = beta
        self.h0 = h0_local
        self.omega_m = omega_m
        self.omega_lambda = 1 - omega_m
        self.c_base = 299792458  # m/s

    def vsl_factor(self, z):
        """Variable Speed of Light factor from UDVT v2.0"""
        # c(z) = c0 * (1 + z)^beta (Power-law VSL model)
        return (1 + z)**self.beta

    def udvt_h_z(self, z):
        """Modified Hubble parameter H(z) including VSL correction"""
        v_factor = self.vsl_factor(z)
        # UDVT correction: H_udvt^2 = H0^2 * [Omega_m(1+z)^3 + Omega_L * v_factor^2]
        h_sq = self.h0**2 * (self.omega_m * (1+z)**3 + self.omega_lambda * v_factor**2)
        return np.sqrt(h_sq)

    def lcdm_h_z(self, z, h0_planck=67.4):
        """Standard LCDM H(z) for comparison"""
        h_sq = h0_planck**2 * (self.omega_m * (1+z)**3 + (1 - self.omega_m))
        return np.sqrt(h_sq)