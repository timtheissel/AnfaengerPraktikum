import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

f,a,b = np.genfromtxt('DatenGES5d.txt', unpack=True)

p = a/b * 2* np.pi

plt.plot(f, p, 'r.',label=r'Messwerte')
plt.xscale('log')
plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])

def trick(x):
    return np.pi * 0.75+ 0*x

l2 = np.linspace(25.22, 28.22, 12)
plt.plot(l2, trick(l2),label=r'$\varphi = \frac{3}{4}\pi $' )

def trick2(x):
    return np.pi * 0.25+ 0*x
l3 = np.linspace(23.18, 26.18, 12)
plt.plot(l3, trick2(l3),label=r'$\varphi = \frac{1}{4}\pi $')

def trick17(x):
    return np.pi * 0.5+ 0*x
l3 = np.linspace(24.22, 27.22, 12)
plt.plot(l3, trick17(l3),label=r'$\varphi = \frac{1}{2}\pi $')

def sigmoid(x, a, b, c):
    return a / (1 + np.exp(-(x - b))) + c

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, f, p, p0=(1, 10, 0))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
a =    3.348 #± 0.127
b =   25.800 #± 0.192
c =   -0.040 #± 0.097
l = np.linspace(20, 32 ,10000)
plt.plot(l, sigmoid(l, a,b,c),label=r'Ausgleichsrechnung')

j = ufloat( 3.348, 0.127)
k = ufloat( 25.800, 0.192)
m = ufloat( -0.040, 0.097)
q = j/((np.pi*0.25)-m)
#print(q)
w = q -1
#print(w)
e = unp.log(w)
#print(e)
r = -e+k 
print(r)

def trick3(x):
    return 24.68+ 0*x
i = np.linspace(0.3, 1.3, 7)
plt.plot(trick3(p), i,label=r'$v_1$')

u= j/((np.pi*0.75)-m)
w = u -1
#print(w)
e = unp.log(w)
#print(e)
r = -e+k 
print(r)

def trick4(x):
    return 26.72+ 0*x
i = np.linspace(1.9, 2.9, 7)
plt.plot(trick4(p), i,label=r'$v_2 $')

u2= j/((np.pi*0.5)-m)
w = u2 -1
#print(w)
e = unp.log(w)
#print(e)
r = -e+k 
print(r)

def trick5(x):
    return 25.72+ 0*x
i = np.linspace(1, 2, 7)
plt.plot(trick5(p), i,label=r'$v_{res} $')


plt.xlabel(r'Frequenz [Hz]')
plt.ylabel(r'Phasenverschiebung [rad]')
plt.title(r"Halblogarithmische Darstellung der Phasenverschiebung")
plt.legend()

plt.show()

#print(p)