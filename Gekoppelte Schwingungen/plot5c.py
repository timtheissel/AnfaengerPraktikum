import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x, y = np.genfromtxt('DatenGES5c.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$U_C/U$')


def trick4(x):
    return 26+ 0*x
i = np.linspace(0, 3.8, 17)
plt.plot(trick4(y), i, label=r'Resonanzüberhöhung')


plt.xscale('log')
plt.xlabel(r'Frequenz [kHz]')
plt.ylabel(r'$U_C/U$')
plt.title(r"Halblogarithmische Darstellung")
plt.legend()
plt.savefig('5c.png')
plt.show()
