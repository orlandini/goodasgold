from ..drude import drude_lorentz
from ..brendelbormann import brendel_bormann
from ..convert import um_to_ev


def au_dl(wl: float):
    """

    Calculates the complex relative permittivity of gold based on Drude-Lorentz model
    Parameters were taken from
    Optical properties of metallic films for vertical-cavity optoelectronic devices
    Aleksandar D. Rakić, Aleksandra B. Djurišić, Jovan M. Elazar, and Marian L. Majewski

    All quantities are dimensionless or eV

    Parameters
    ----------
    wl = wavelength (um)
    """
    wp = 9.03  # eV
    f0 = 0.760
    g0 = 0.053  # eV
    # oscillator strength, damping constant and frequency

    interband = [(0.024, 0.241, 0.415),
                 (0.010, 0.345, 0.830),
                 (0.071, 0.870, 2.969),
                 (0.601, 2.494, 4.304),
                 (4.384, 2.214, 13.32)]  # dimensionless, eV, eV, eV
    er = drude_lorentz(um_to_ev(wl), wp, f0, g0, interband)
    return [er.real, er.imag]


def au_bb(wl: float):
    """

    Calculates the complex relative permittivity of gold based on Brendel-Bormann model
    Parameters were taken from
    Optical properties of metallic films for vertical-cavity optoelectronic devices
    Aleksandar D. Rakić, Aleksandra B. Djurišić, Jovan M. Elazar, and Marian L. Majewski

    All quantities are dimensionless or eV

    Parameters
    ----------
    wl = wavelength (um)
    """
    wp = 9.03  # eV
    f0 = 0.770
    g0 = 0.050  # eV

    interband = [(0.054, 0.074, 0.218, 0.742),
                 (0.050, 0.035, 2.885, 0.349),
                 (0.312, 0.083, 4.069, 0.830),
                 (0.719, 0.125, 6.137, 1.246),
                 (1.648, 0.179, 27.97, 1.795)]  # dimensionless, eV, eV, eV
    er = brendel_bormann(um_to_ev(wl), wp, f0, g0, interband)
    return [er.real, er.imag]
