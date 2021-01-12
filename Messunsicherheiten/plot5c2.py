import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x, y = np.genfromtxt('DatenGES5c2.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$u_C/U$')


def sigmoid(x):
    return 3.8/np.sqrt(2) +0*x

plt.plot(x, sigmoid(x),label=r'$ q * \frac{1}{\sqrt{2}} $')




def fit(x, a, b,c):
    return a*(x-b)**2+c

x, y = np.loadtxt('DatenGES5c2.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(fit, x, y, p0=(-1, 26, 3.8), maxfev=1000000000)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abcd', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

a = -0.064195# ± 0.006518
b = 25.670798# ± 0.144380
c = 3.677980# ± 0.070971
l = np.linspace(21, 30 ,10000)
plt.plot(l, fit(l, a,b,c),label=r'Ausgleichsrechnung')

n = 3.8/np.sqrt(2)
v2 = (n-c)/a
v = np.sqrt((n-c)/a)+b
v1 = -np.sqrt((n-c)/a)+b
print(v)
def trick4(x):
    return 21.74181111446039+ 0*x
i = np.linspace(2.4, 3, 8)
plt.plot(trick4(y), i, label=r'$v_-$')

def trick5(x):
    return 29.599784885539613+ 0*x
i = np.linspace(2.4, 3, 8)
plt.plot(trick5(y), i, label=r'$v_+$')



plt.xlabel(r'Frequenz [Hz]')
plt.ylabel(r'$U_C/U$')
plt.title(r"Lineare Darstellung um die Resonanzfrequenz")
plt.legend()
plt.grid()
plt.savefig('5c.png')

plt.show()