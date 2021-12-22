import numpy as np


def um_to_thz(wl: float):
    """
    Converts from wavelength (um)
    to frequency (THz))



    Parameters
    ----------
    wl: float
        wavelength

    """
    return 299.793458/wl  # speed of light/10**6


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
    delta = np.sqrt(er1**2+er2**2)
    n = np.sqrt((delta+er1)/2)
    k = np.sqrt((delta-er1)/2)
    return [n, k]
