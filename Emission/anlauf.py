import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

x, y  = np.genfromtxt('Anlauf.txt', unpack=True)
f = 1.602 * 10e-19
k = 1.380 * 10e-23
def sigmoid(x, a, b):
    return a*np.exp(-(f*x)/(k*b))

l = np.linspace(0, 1, 50)
plt.plot(x, y, 'r.', label=r'Messwerte')
plt.plot(l, sigmoid(l, 12.254, 1900.685), label=r'Fit')
plt.xlabel(r'angelegte Spannung [V]')
plt.ylabel(r'Anodenstrom [A]')
plt.legend()
plt.title(r"Anlaufstromgebiet")
plt.savefig('Anlauf.png')
plt.show()





from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y, p0=(0,1500))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')


