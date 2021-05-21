import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

w, N0 = np.genfromtxt('ComptonOhne.txt', unpack=True)

N1 = np.genfromtxt('ComptonAl.txt', unpack=True)

NO = unp.uarray(N0, np.sqrt(N0*200)/200)

NA = unp.uarray(N1, np.sqrt(N1*200)/200)

t = 90e-6

I0 = NO/(1-t*N0)
IA = NA/(1-t*NA)
#print(I0)
#print(IA)

T = IA/I0
#print(T)

d = 2.014e-10

l = 2*d*np.sin((w*np.pi)/180)
print(l)
def fit(x, a, b):
    return a*x+b
plt.errorbar(l,unp.nominal_values(T), yerr=unp.std_devs(T), fmt='g.', label=r'Messwerte mit Fehler')
plt.plot(l, fit(l,-15194.73e6,1.225), 'r-', label=r'Ausgleichsgerade')
plt.legend()
plt.title('Transmission als Funktion der Wellenlänge')
plt.ylabel(r'Transmission')
plt.xlabel(r'Wellenlänge $\lambda$ [m]')
plt.savefig('Transmission.png')
#plt.show()



#params, covariance_matrix = curve_fit(fit, l, unp.nominal_values(T), p0=(-15194,1.225))

#uncertainties = np.sqrt(np.diag(covariance_matrix))

#for name, value, uncertainty in zip('ab', params, uncertainties): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

I = 2731
I1 = 1180
I2 = 1024

T1 = I1/I
print(T1)
T2 = I2/I 

a = ufloat(-15194.73e6 , 239.10e6)
b = ufloat(1.225, 0.014)

l1 = (T1-b)/a
print(l1)
l2 = (T2-b)/a
print(l2)
print(l2-l1)