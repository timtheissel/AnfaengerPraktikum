import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

t, N2 = np.genfromtxt('Vanadium.dat', unpack=True)

N3 = N2 - 14
errY = np.sqrt(N3) 

plt.errorbar(t,N3, errY, fmt='.', label=r'Messwerte')

def sigmoid(t, a, b):
    return (a * np.exp(-b*t)) 

x, y = np.loadtxt('Vanadium.dat', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y ,p0=(205, 0.0035))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
   print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

c = np.linspace(0, 1500,2000)



l = ufloat(0.002657, 0.000106)
T = np.log(2)/l
print(T)

x, y = np.loadtxt('Vanadium.dat', unpack=True)
from scipy.optimize import curve_fit
params2, covariance_matrix1 = curve_fit(sigmoid, x[:18], y[:18] ,p0=(205, 0.0035))

uncertainties = np.sqrt(np.diag(covariance_matrix1))

for name, value, uncertainty in zip('abc', params2, uncertainties): 
   print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

l2 = ufloat(0.002937, 0.000170)
T2 = np.log(2)/l2
print(T2)


plt.plot(c, sigmoid(c, 208.761825, 0.002657), label=r'Ausgleichsrechnung 1')
plt.plot(c, sigmoid(c, 218.126931, 0.002937), label=r'Ausgleichsrechnung 2')
plt.yscale('log')
plt.xlabel(r'Zeit[s]')
plt.ylabel(r'N [Imp]')
plt.legend()
plt.title(r"Vanadium")
plt.savefig('22.png')
plt.show()