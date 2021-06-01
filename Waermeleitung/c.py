import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('c.dat', unpack=True)

plt.figure()
plt.plot(x/2, T7, label=r'T7')
plt.plot(x/2, T8, label=r'T8')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T7 und T8')
plt.savefig('steel.png')
plt.show()