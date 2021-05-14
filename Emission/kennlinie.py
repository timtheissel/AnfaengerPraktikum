import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

x, y1, y2, y3, y4, y5  = np.genfromtxt('Kennlinie.txt', unpack=True)

plt.plot(x, y1, 'r.', label=r'Kennlinie 1')
plt.plot(x, y2, 'b.', label=r'Kennlinie 2')
plt.plot(x, y3, 'g.', label=r'Kennlinie 3')
plt.plot(x, y4, 'y.', label=r'Kennlinie 4')
plt.plot(x, y5, 'm.', label=r'Kennlinie 5')
plt.xlabel(r'angelegte Spannung [V]')
plt.ylabel(r'Anodenstrom [A]')
plt.legend()
plt.title(r"Kennlinienschar")
plt.savefig('Kennlinie1.png')
plt.show()




e = 8.854 * 10e-12
f = 1.602 * 10e-19
m = 9.109 * 10e-31

x, b, c, d, e, y5  = np.genfromtxt('Kennlinie2.txt', unpack=True)
def sigmoid(x, a, b):
    return b*x**a

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y5, p0=(1.5, 0.002))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, y5, 'm.')
plt.plot(x, sigmoid(x, 1.437, 0.001))
plt.xlabel(r'angelegte Spannung [V]')
plt.ylabel(r'Anodenstrom [A]')
plt.title(r"Heizspannung=5.5V, Heizstrom=2.5A ")

plt.savefig('LS.png')
plt.show()