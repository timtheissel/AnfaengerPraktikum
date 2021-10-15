import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

f, U = np.genfromtxt('durchlass.dat', unpack=True)

def fit(x, a, b, c, d, e, f):
    return a * np.exp((-(x-b)**2/2*c)) + (d / (1+((x-e)/f)**2))


from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(fit, f, U/11, p0=(-0.605, 21.753, 1.145, 1.544, 21.825, 0.852))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abcdef', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

x = np.linspace(0, 40, 40000)
plt.plot(f, U/11, 'rx', label=r'Messwerte')
plt.plot(x, fit(x, -0.605, 21.753, 1.145, 1.544, 21.825, 0.852), label=r'fit')
plt.legend()
plt.xlabel('$ f \; [kHz]$')
plt.ylabel('$ U_A/U_E \; [V]$')
plt.savefig('durchlass.png')
plt.show()

dwDy = 7800
dwGd = 7400

QDy = 0.0151/(0.147*dwDy)
#print('QDy', QDy)

QGa = 0.015/(0.1408*dwGd)
#print('QGa', QGa)

R3 = [3.395, 3.390, 3.365]
R3Dy = [1.845, 1.865, 1.865]
Ubr0 = [0.000085, 0.000111, 0.0001]
Ubr = [0.00175, 0.00175, 0.0017]

def XU(x):
    return 4 * ((86.6e-6)/QDy) * (x/1) / 10

def XR(x):
    return 2 * (x/1000) * ((86.6*10**-6)/QDy)

#print(XU(0.01665))
#print(XU(0.01639))
#print(XU(0.016))
#
#print(XR(1.55))
#print(XR(1.525))
#print(XR(1.5))

def XU(x):
    return 4 * ((86.6e-6)/QGa) * (x/1) / 10

def XR(x):
    return 2 * (x/1000) * ((86.6*10**-6)/QGa)

#print(XU(0.0077))
#print(XU(0.0076))
#print(XU(0.0077))
#
#print(XR(0.725))
#print(XR(0.745))
#print(XR(0.74))

v_0 = ufloat(21.753, 0.115)
v_1 = ufloat(20.89, 0.03)
v_2 = ufloat(22.76, 0.03)

print(v_0/(v_2 -v_1))