import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x,y = np.genfromtxt('DatenGES.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'Messwerte')


def sigmoid(x, a, b):
    return b*np.exp(-2 * np.pi * a * x)

x, y = np.loadtxt('DatenGES.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y, p0=(0, 4))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

#a = 0.001218 ± 0.000017 1 durch mikrosekunde also mal 
#b = 4.033851 ± 0.035089 Volt

l = np.linspace(0, 350, 1000)
plt.plot(l, sigmoid(l, 0.0012, 4.034) ,label=r'Ausgleichsrechnung')

plt.xlabel(r'Zeit [µs]')
plt.ylabel(r'Spannungsamplituden [V]')

plt.legend()
plt.grid()
plt.savefig('5a.png')
#plt.show()
a = ufloat(1218, 17)
L = ufloat(0.01678,0.00009)
R = 4 * np.pi * L *a
T = 1 / ( 2 * np.pi * a)
print(R)
print(T)