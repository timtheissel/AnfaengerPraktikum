import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

f, A = np.genfromtxt('2.txt', unpack=True)

U0 = 15
x = np.linspace(0, 10000, 10000)
def fit(x, A, b):
   return A / np.sqrt(1 + b**2 * x**2)

plt.plot(f, (A/U0), 'rx', label=r'Messwerte')
plt.xscale('log')
plt.plot(x, fit(x, 0.53971, 0.01453), label=r'fit')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('$ \ln(U_C/U_0) $')
plt.title('Frequenzabhängigkeit der Amplitude')
plt.savefig('2.png')
plt.show()


params, covariance_matrix = curve_fit(fit, f, A/U0, p0=(0, 1)) 

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.5f} ± {uncertainty:.5f}')
