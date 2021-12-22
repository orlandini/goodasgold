from scipy.interpolate import interp1d
import numpy as np
import csv

# all the data was taken from the supporting information of
# Ultrathin and Ultrasmooth Gold Films on Monolayer MoS2
# by Dmitry I. Yakubovsky, Yury V. Stebunov, Roman V. Kirtaev,
# Georgy A. Ermolaev, Mikhail S. Mironov, Sergey M. Novikov,
# Aleksey V. Arsenin, and Valentyn S. Volkov*


# available data is from the range 0.3um to 3.3um and was found at
# https://refractiveindex.info/


def _au_data(which):
    """
    Gets gold data from csv file for a given layer width



    Parameters
    ----------
    which: int
        0 for 4nm, 1 for 6.1nm and 2 for 9nm

    """
    assert which >= 0
    assert which <= 2
    assert type(which) == int
    width = '4' if which == 0 else '6_1' if which == 1 else '9'
    with open('data/au_'+width+'mm_yakubovsky19.csv', newline='') as csvfile:
        data = np.array(list(csv.reader(csvfile)))

    x = data[1:, 0].astype('float')
    n = data[1:, 1].astype('float')
    k = data[1:, 2].astype('float')
    f1 = interp1d(x, n+k*1j, kind='cubic')
    # f2 = interp1d(x, e_imag, kind='cubic')

    return f1


def _au_4nm(wl):
    """
    For a given input in um, gives n and k
    """
    return _au_data(0)(wl)[()]


def _au_6_1nm(wl):
    """
    For a given input in um, gives n and k
    """
    return _au_data(1)(wl)[()]


def _au_9nm(wl):
    """
    For a given input in um, gives n and k
    """
    return _au_data(2)(wl)[()]


au_4nm = _au_4nm
au_6_1nm = _au_6_1nm
au_9nm = _au_9nm

del _au_4nm
del _au_6_1nm
del _au_9nm
