import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

y, x  = np.genfromtxt('diffenv.txt', unpack=True)

plt.plot(x, y, 'r.', label=r'Messwerte')

plt.xlabel(r'Bremsspannung [V]')
plt.ylabel(r'Steigung')
plt.legend()
plt.title(r"differentielle Energieverteilung T=23$^\circ C$")
plt.savefig('8a1.png')
plt.show()

y2, x2  = np.genfromtxt('diffenv2.txt', unpack=True)
plt.plot(x2, y2, 'r.', label=r'Messwerte')

plt.xlabel(r'Bremsspannung [V]')
plt.ylabel(r'Steigung')
plt.legend()
plt.title(r"differentielle Energieverteilung T=155$^\circ C$")
plt.savefig('8a2.png')
plt.show()
