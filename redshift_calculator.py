### redshift_calculator.py

from astropy.constants import c
import numpy as np

# Hubble constant (km/s/Mpc)
H0 = 70  # You can make this adjustable in the app later


def relativistic_velocity(z):
    """
    Calculate recession velocity using the relativistic Doppler formula.
    v = c * ((z+1)^2 - 1) / ((z+1)^2 + 1)
    """
    z_plus = (z + 1)
    beta = ((z_plus ** 2) - 1) / ((z_plus ** 2) + 1)
    return beta * c.to('km/s').value


def hubble_distance(velocity):
    """
    Distance using Hubble's Law: d = v / H0
    Result in Megaparsecs (Mpc)
    """
    return velocity / H0


def light_travel_time(distance):
    """
    Time = distance / speed of light
    Convert Mpc to km to match units
    Return time in billions of years
    """
    distance_km = distance * 3.08567758e19  # Mpc to km
    time_sec = distance_km / c.value
    time_years = time_sec / (60 * 60 * 24 * 365.25)
    return time_years / 1e9
