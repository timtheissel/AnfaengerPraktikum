import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('1.dat', unpack=True)

plt.figure()
plt.plot(x/5, T1, 'r-', label=r'T1')
plt.plot(x/5, T4, 'b-', label=r'T4')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T1 und T4')
plt.savefig('1.png')
plt.show()

plt.figure()
plt.plot(x/5, T5, 'r-', label=r'T5')
plt.plot(x/5, T8, 'b-', label=r'T8')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T5 und T8')
plt.savefig('2.png')
plt.show()

plt.figure()
plt.plot(x/5, T7-T8, 'r-', label=r'T7-T8')
plt.plot(x/5, T2-T1, 'b-', label=r'T2-T1')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturdifferenzen ')
plt.savefig('3.png')
plt.show()