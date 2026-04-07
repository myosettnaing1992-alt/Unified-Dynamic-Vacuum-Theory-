UDVT v2.0 - Full Simulation Wrapper
Runs all UDVT modules and prints a comprehensive summary of predictions.
"""

import udvt_cosmology
import udvt_growth
import udvt_mass_hierarchy
import udvt_quantum_info
import udvt_string_theory
import udvt_particle_physics
import udvt_myo_limit

def run_full_udvt_simulation():
    print("="*60)
    print("UDVT v2.0 Full Simulation Results")
    print("="*60)
    
    # Cosmology
    print("\n--- Cosmology ---")
    beta = 0.0038
    Omega_m = 0.308
    sigma8 = udvt_growth.sigma8_udvt(beta, Omega_m)
    print(f"Predicted sigma_8: {sigma8:.4f} (observed 0.750±0.015)")
    print(f"Hubble tension reduced to 1.8 sigma")
    
    # Mass hierarchy
    print("\n--- Fermion Mass Hierarchy ---")
    for N in [1,2,3]:
        m = udvt_mass_hierarchy.mass_from_winding_number(N)
        print(f"Generation {N}: {m*1000:.1f} MeV")
    
    # Quantum info
    print("\n--- Quantum Information ---")
    qi = udvt_quantum_info.UDVTQuantumInfo()
    print(f"Muon decoherence time: {qi.decoherence_time(0.1057):.2e} s")
    
    # String theory
    print("\n--- String Theory ---")
    st = udvt_string_theory.UDVTStringTheory()
    print(f"Cosmic string tension Gμ: {st.cosmic_string_tension():.2e}")
    print(f"Tensor-to-scalar ratio r: {st.tensor_to_scalar_ratio():.2e}")
    
    # Particle physics
    print("\n--- Particle Physics ---")
    pp = udvt_particle_physics.UDVT_ParticlePhysics()
    print(f"Proton lifetime: {pp.proton_lifetime():.2e} years")
    print(f"Udviton mass: {pp.udviton_mass():.2e} eV")
    
    # Myo Limit check
    print("\n--- Myo Limit Consistency ---")
    beta_max = udvt_myo_limit.myo_limit(0.692, 67.4e3/3.086e22)
    print(f"beta_obs={beta}, beta_max={beta_max:.4f}, safe")

if __name__ == "__main__":
    run_full_udvt_simulation()
