import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

e, U = np.genfromtxt('1.txt', unpack=True)
def fit(x, a, b):
   return (-1/a)*x+b
u = (U/1)
print(u)

t = e*0.001

plt.plot(t, np.log(u), 'r.', label=r'Messwerte')
plt.plot(t, fit(t, 0.00895, -0.2083), label=r'fit')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('$ \ln(U_C/U_0) $')
plt.title('Entladekurve')
plt.savefig('1.png')
plt.show()




params, covariance_matrix = curve_fit(fit, t, np.log(u), p0=(0.007, -0.209)) 

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.5f} ± {uncertainty:.5f}')


