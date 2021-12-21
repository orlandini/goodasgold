import matplotlib.pyplot as plt
import numpy as np

from goodasgold.models import rakic98
from goodasgold.convert import nk_from_er

if __name__ == "__main__":

    fig = plt.figure()
    ax = plt.axes()

    wl = np.linspace(0.2, 1.5, 100)
    er = [rakic98.au_dl(w) for w in wl]
    n = [nk_from_er(e[0], e[1])[0] for e in er]
    k = [nk_from_er(e[0], e[1])[1] for e in er]
    ax.plot(wl, n)
    ax.plot(wl, k)
    plt.show()
