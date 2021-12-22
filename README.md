# good as gold

Small library for calculating and experimenting with optical properties of conductors.

## available models
- Drude-Lorentz
- Brendel-Bormann

## available data

### Gold
- rakic98.au_dl : Drude-Lorentz model for gold. Data taken from *Optical properties of metallic films for vertical-cavity optoelectronic devices* by Aleksandar D. Rakić, Aleksandra B. Djurišić, Jovan M. Elazar, and Marian L. Majewski. [https://doi.org/10.1364/AO.37.005271](https://doi.org/10.1364/AO.37.005271)
- rakic98.au_bb : Brendel-Bormann model for gold. Data taken from *Optical properties of metallic films for vertical-cavity optoelectronic devices* by Aleksandar D. Rakić, Aleksandra B. Djurišić, Jovan M. Elazar, and Marian L. Majewski. [https://doi.org/10.1364/AO.37.005271](https://doi.org/10.1364/AO.37.005271)
- yakubovsky19(.au_4nm|.au_6_1nm|.au_9nm) : Experimental data for thin layers of gold. Data taken from *Ultrathin and Ultrasmooth Gold Films on Monolayer MoS2* by Dmitry I. Yakubovsky, Yury V. Stebunov, Roman V. Kirtaev, Georgy A. Ermolaev, Mikhail S. Mironov, Sergey M. Novikov, Aleksey V. Arsenin, and Valentyn S. Volkov. [https://doi.org/10.1002/admi.201900196][https://doi.org/10.1002/admi.201900196]


## contributing with your own data

See 

- `rakic98.au_dl` for how to import a Drude-Lorentz model
- `rakic98.au_bb` for how to import a Brendel-Bormann model
- `yakubovsky19` for how to import experimental data in .csv format