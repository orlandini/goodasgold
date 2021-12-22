import matplotlib.pyplot as plt
import numpy as np

from goodasgold.models import rakic98
from goodasgold.convert import er_to_nk

if __name__ == "__main__":

    fig = plt.figure()

    wl = np.linspace(0.2, 1.5, 100)
    er = np.array([rakic98.au_dl(w) for w in wl])
    [n, k] = er_to_nk(er[:, 0], er[:, 1])

    plt.plot(wl, n, label="n")
    plt.plot(wl, k, label="k")
    plt.xlabel('Wavelength (μm)')
    plt.ylabel('n, k')

    plt.legend(loc="upper left")

    plt.show()
