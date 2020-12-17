import math
import scipy.stats

import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 
from scipy.optimize import curve_fit

d, N = np.genfromtxt('daten3.txt', unpack=True)

print(np.sqrt(N))


plt.errorbar(d,N, yerr=np.sqrt(N)*3, fmt='g.', label=r'Messwerte mit Fehler')

def fit(d, a, m):
    return a*np.exp(-m*d)

params, covariance_matrix = curve_fit(fit, d, N)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('amd', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

#mitfehler
t = np.linspace(0,5,500)
plt.plot(t, fit(t, *params), label=r'fit')
plt.yscale('log')
plt.legend()
plt.xlabel(r'Dicke d [cm]')
plt.ylabel(r'Gamma-Quanten N')
plt.title(r'lin-log-Darstellung')
plt.savefig('4.png')

plt.show()