import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('b.dat', unpack=True)

plt.figure()
plt.plot(x/2, T1, label=r'T1')
plt.plot(x/2, T2, label=r'T2')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T1 und T2')
plt.savefig('brass.png')
plt.show()

plt.figure()
plt.plot(x/2, T6, label=r'T6')
plt.plot(x/2, T5, label=r'T5')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T5 und T6')
plt.savefig('alu.png')
plt.show()