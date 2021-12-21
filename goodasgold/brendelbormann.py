import numpy as np
from typing import List
from scipy.special import wofz


def brendel_bormann(wl: float, w_p: float, f_0: float, g_0: float,
                    bound_electron_params: List[tuple]):
    π = np.pi
    """
    Implements the Brendel-bormann model for conductors

    1 - f_0 Omega_p^2/(w(w-i Gamma_0))
    + sum_j^k (f_j w_p)/(w_j^2-w^2) + i w Gamma_j


    where Omega_p = sqrt(f_0) w_p

    wofz is the Fadeeva function
    exp(-z**2)*erfc(-j*z)

    special thanks to https://github.com/polyanskiy/refractiveindex.info-scripts
    Parameters
    ----------
    w_p: float
        plasma frequency (ev)
    f_0: float
        oscillator strength of intraband transitions
    g_0: float
        damping constant of intraband transitions
    bound_electron_params: List[tuple]
        interband parameters f_i, Gamma_i, w_i and sigma_i
    wl: float
        input frequency/wavelength/eV

    """

    epsilon = 1 - f_0*w_p*w_p/(wl*(wl - 1j * g_0))
    for [fi, gi, wi, si] in bound_electron_params:

        alpha = (wl**2+1j*wl*gi)**.5
        za = (alpha-wi)/(2**.5*si)
        zb = (alpha+wi)/(2**.5*si)
        epsilon += 1j*π**.5*fi*w_p**2 / (2 **
                                         1.5*alpha*si) * (wofz(za)+wofz(zb))  # χi
    return epsilon
