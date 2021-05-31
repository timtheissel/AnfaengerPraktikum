import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

f, a, b = np.genfromtxt('3.txt', unpack=True)

p = (a/b) * 2 * np.pi

def fit(x, a, b):
   return b * np.arctan(a*x)

x = np.linspace(10, 10000, 10000)

plt.plot(f, p, 'rx', label=r'Messwerte')
plt.plot(x, fit(x, 0.01656, 1.0532), label=r'Messwerte')
plt.xscale('log')
plt.legend()
plt.xlabel('f [Hz]')
plt.ylabel('$ \phi [rad] $')
plt.title('Frequenzabhängigkeit der Phasenverschiebung')
plt.savefig('3.png')
plt.show()



params, covariance_matrix = curve_fit(fit, f, p, p0=(0.027, 0.88), maxfev=5000000) 

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.5f} ± {uncertainty:.5f}')



