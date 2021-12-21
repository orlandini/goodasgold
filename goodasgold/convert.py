from scipy.constants import speed_of_light
from math import sqrt


def um_to_thz(wl: float):
    """
    Converts from wavelength (um)
    to frequency (THz))



    Parameters
    ----------
    wl: float
        wavelength

    """
    return speed_of_light/(wl * 10**6)


def thz_to_ev(freq: float):
    """
    Converts a operational frequency (THz)
    to electronvolts (eV)



    Parameters
    ----------
    freq: float
        frequency (THz)

    """
    return freq/(241.799050402293)


def um_to_ev(wl: float):
    """
    Converts from wavelength (um)
    to electronvolts (eV)




    Parameters
    ----------
    wl: float
        wavelength (um)

    """
    return thz_to_ev(um_to_thz(wl))


def nk_from_er(er1: float, er2: float):
    """
    Calculates the refractive index based on the relative permittivity
    The refractive index is given by n - jk


    Parameters
    ----------
    er1: float
        real part of relative permittivity
    er2: float
        imaginary part of relative permittivity
    """
    delta = sqrt(er1**2+er2**2)
    n = sqrt((delta+er1)/2)
    k = sqrt((delta-er1)/2)
    return [n, k]
