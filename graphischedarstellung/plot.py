import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x,y = np.genfromtxt('daten.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'Messwerte')

def sigmoid(x, a, b):
    return a*x+b

x, y = np.loadtxt('daten.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

#a=5 .6 +- 0.825 b=0.008 +- 0.003

plt.plot(x, sigmoid(x, 5.6, 0.008), label=r'fit')

plt.xlabel(r'Masse [kg]')
plt.ylabel(r'Auslenkung x [m]')
plt.legend()
plt.title(r"m-x Diagramm")
plt.savefig('1.png')
plt.show()

a = ufloat(5.6, 0.825)

k = 9.81/a 
#print(k)