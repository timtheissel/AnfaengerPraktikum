import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 


x,y = np.genfromtxt('Kennlinie.dat', unpack=True)

errY = np.sqrt(y) 

plt.errorbar(x,y, errY, fmt='.', label=r'Messwerte')



def sigmoid(x, a, b):
    return a*x+b

x, y = np.loadtxt('Kennlinie2.dat', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
   print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

l = np.linspace(370, 640, 28)
plt.plot(l, sigmoid(l, 1.151888, 9584.296388), label=r'Ausgleichsrechnung')

m = ufloat(1.151888 , 0.223673)
ps = (m/60)*100
print(ps.n)
print(ps.s)
plt.xlabel(r'Gemessene Impulse [$\frac{Imp}{60s}$]')
plt.ylabel(r'Auslenkung x [m]')
plt.legend()
plt.title(r"Charakteristik eines Geiger-Müller Zählrohrs")
plt.savefig('7a.png')
plt.show()
