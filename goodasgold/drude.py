from typing import List


def drude_lorentz(wl: float, w_p: float, f_0: float, g_0: float,
                  bound_electron_params: List[tuple]):
    """
    Implements the drude-lorentz model for conductors

    1 - f_0 Omega_p^2/(w(w-i Gamma_0))
    + sum_j^k (f_j w_p)/(w_j^2-w^2) + i w Gamma_j


    where Omega_p = sqrt(f_0) w_p
    Parameters
    ----------
    w_p: float
        plasma frequency (ev)
    f_0: float
        oscillator strength of intraband transitions
    g_0: float
        damping constant of intraband transitions
    bound_electron_params: List[tuple]
        interband parameters f_i, Gamma_i and w_i
    wl: float
        input frequency/wavelength/eV

    """

    # intraband contribution
    epsilon = 1 - f_0*w_p*w_p/(wl*(wl - 1j * g_0))

    # interband contributions
    for[f_i, g_i, w_i] in bound_electron_params:
        epsilon += (f_i * w_p * w_p) / (w_i ** 2 - wl ** 2 + wl * g_i * 1j)

    return epsilon
