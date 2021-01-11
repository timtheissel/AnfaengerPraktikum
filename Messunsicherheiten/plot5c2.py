import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x, y = np.genfromtxt('DatenGES5c2.txt', unpack=True)
plt.plot(x, y, 'r.')


def sigmoid(x):
    return 3.8/np.sqrt(2) +0*x

plt.plot(x, sigmoid(x))




#def fit(x, a, b, c):
#    return a*x**c+b
#
#x, y = np.loadtxt('DatenGES5c2.txt', unpack=True)
#from scipy.optimize import curve_fit
#params, covariance_matrix = curve_fit(fit, x, y)
#
#uncertainties = np.sqrt(np.diag(covariance_matrix))
#
#for name, value, uncertainty in zip('abc', params, uncertainties): 
#    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

#plt.plot(x, fit(x, 0.0000, 3.14))


plt.show()