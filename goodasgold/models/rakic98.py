from ..drude import drude_lorentz
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
    wp = 9.03
    f0 = 0.760
    g0 = 0.053
    # oscillator strength, damping constant and frequency
    interband = [(0.024, 0.241, 0.415),
                 (0.010, 0.345, 0.830),
                 (0.071, 0.870, 2.969),
                 (0.601, 2.494, 4.304),
                 (4.384, 2.214, 13.32)]
    er = drude_lorentz(um_to_ev(wl), wp, f0, g0, interband)
    return [er.real, er.imag]
