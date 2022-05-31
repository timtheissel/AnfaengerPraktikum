import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

I, B = np.genfromtxt('eichmagnet.txt', unpack=True)


params, covariance_matrix = np.polyfit(I, B, deg=2, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('abc', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')


plt.plot(I, B, 'r.', label=r'Messwerte')
plt.plot(I, -5.93*I**2 + 121.318*I-20.926, label=r'Ausgleichsrechnung')
plt.xlabel(r'I [A]')
plt.ylabel(r'B [mT]')
plt.title(r"I-B Diagramm")
plt.legend()
plt.savefig('magnet.png')
plt.show()

def B(I):
    return -5.93*I**2 + 121.318*I-20.926

print(B(7.8))

print(B(4))
