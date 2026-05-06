import numpy as np

def calculate_chi_square(observed, predicted, errors):
    """Calculates Chi-square to validate UDVT against observational data"""
    return np.sum(((observed - predicted) / errors) ** 2)

# Example Validation (Mock Data from Planck/JWST)
obs_h0 = 73.0  # Local measurement (SH0ES)
pred_h0 = 71.2 # UDVT Prediction
error_h0 = 1.4

chi2 = calculate_chi_square(obs_h0, pred_h0, error_h0)
print(f"UDVT Statistical Confidence (Chi2): {chi2:.4f}")
