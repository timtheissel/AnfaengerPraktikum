import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

x, beb, keb, kee, bee, grb, krb, x2, gre, kre = np.genfromtxt('Messwerte.txt', unpack=True)

def linear(x, a, b):
    return a*x+b

L = 0.54
X = L*(x/100)**2-((x/100)**3/3)
X2 = L*(x2/100)**2-((x2/100)**3/3)

plt.figure()
plt.plot(X, kee/1000, 'r.', label=r'kupfern eckig')
plt.plot(X, linear(X, 0.051148, 0.000015), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('kee.png')
plt.show()








plt.figure()
plt.plot(X, bee/1000, 'g.', label=r'braun eckig')
plt.plot(X, linear(X, 0.027832, 0.000093), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('bee.png')
plt.show()



plt.figure()
plt.plot(X2, gre/1000, 'g.', label=r'golden rund')
plt.plot(X2, linear(X2, 0.061902, 0.000126), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('gre.png')
plt.show()

plt.figure()
plt.plot(X2, kre/1000, 'r.', label=r'kupfern rund')
plt.plot(X2, linear(X2, 0.017019, 0.000033), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('kre.png')
plt.show()



x, beb, keb, kee, bee, grb, krb, x2, gre, kre = np.genfromtxt('beidlinks.txt', unpack=True)

L = 0.55

Xl = 3*(L**2)*(x/100)-4*(x/100)**3


plt.figure()
plt.plot(Xl, beb/1000, 'r.', label=r'braun eckig')
plt.plot(Xl, linear(Xl, 0.001488, -0.000034), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('beb.png')
plt.show()



plt.figure()
plt.plot(Xl, keb/1000, 'r.', label=r'kupfern eckig')
plt.plot(Xl, linear(Xl, 0.003316, -0.000008), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('keb.png')
plt.show()



plt.figure()
plt.plot(Xl, grb/1000, 'r.', label=r'golden rund')
plt.plot(Xl, linear(Xl, 0.009718, 0.000035), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('grb.png')
plt.show()



plt.figure()
plt.plot(Xl, krb/1000, 'r.', label=r'kupfern rund')
plt.plot(Xl, linear(Xl, 0.002602, -0.000080), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('krb.png')
plt.show()




x, beb, keb, kee, bee, grb, krb, x2, gre, kre = np.genfromtxt('beidrechts.txt', unpack=True)

Xr = 4*(x/100)**3-12*L*(x/100)**2+9*(L**2)*(x/100)-L**3


plt.figure()
plt.plot(Xr, beb/1000, 'r.', label=r'braun eckig')
plt.plot(Xr, linear(Xr, 0.001398, 0.000014), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('beb2.png')
plt.show()

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(linear, Xr, beb/1000)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

plt.figure()
plt.plot(Xr, keb/1000, 'r.', label=r'kupfern eckig')
plt.plot(Xr, linear(Xr, 0.003524, 0.000021), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('keb2.png')
plt.show()

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(linear, Xr, keb/1000)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

plt.figure()
plt.plot(Xr, grb/1000, 'r.', label=r'golden rund')
plt.plot(Xr, linear(Xr, 0.009583, 0.000094), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('grb2.png')
plt.show()

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(linear, Xr, grb/1000)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

plt.figure()
plt.plot(Xr, krb/1000, 'r.', label=r'kupfern rund')
plt.plot(Xr, linear(Xr, 0.002672, 0.000009), 'b', label=r'fit')
plt.legend()
plt.xlabel('$Lx^2-x^3/3$  [m$^3$] ')
plt.ylabel('D(x) [m]')
plt.savefig('krb2.png')
plt.show()

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(linear, Xr, krb/1000)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.6f} ± {uncertainty:.6f}')

