import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

t, N2 = np.genfromtxt('Rhodium.dat', unpack=True)

N = N2 - 7
errY = np.sqrt(N) 

plt.errorbar(t,N, errY, fmt='.', label=r'Messwerte')

def sigmoid(t, a, b):
    return (a * np.exp(-b*t)) 


from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, t[20:], N[20:] ,p0=(70, 0.0020))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
   print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

K = N[0:10] - sigmoid(t[0:10], *params)

from scipy.optimize import curve_fit
params2, covariance_matrix = curve_fit(sigmoid, t[0:10], K ,p0=(70, 0.0020))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params2, uncertainties): 
   print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')



c = np.linspace(0, 640, 1000)
d = np.linspace(0, 300, 400)
plt.plot(c, sigmoid(c, 72.317788, 0.002646), label=r'langlebiger Zerfall')
plt.plot(d, sigmoid(d, *params2), label=r'kurzlebiger Zerfall')
plt.plot(c, (sigmoid(c, *params)+sigmoid(c, *params2)), label=r'kombinierter Zerfall')
plt.yscale('log')
plt.xlabel(r'Zeit[s]')
plt.ylabel(r'N [Imp]')
plt.legend()
plt.title(r"Rhodium")
plt.savefig('3.png')
plt.show()