import numpy as np
from src.utils import R_EARTH, MU_EARTH

def compute_orbital_period(altitude_km):
    r = R_EARTH + altitude_km
    return 2 * np.pi * np.sqrt(np.power(r, 3) / MU_EARTH)

def compute_eclipse_duration(altitude_km):
    r = R_EARTH + altitude_km
    period = compute_orbital_period(altitude_km)
    zeta = np.arcsin(R_EARTH / r)
    return (zeta / np.pi) * period