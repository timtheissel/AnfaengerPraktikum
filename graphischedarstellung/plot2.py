import math
import scipy.stats

import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 


g, b = np.genfromtxt('daten2.txt', unpack=True)

f = (g*b)/(g+b)
print(f, np.sum(f)/6)

print(np.std(f))

print(np.std(f)/math.sqrt(6))


#b)

G=1/g 
#print(G)

B=1/b
params, covariance_matrix = np.polyfit(G, B, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

plt.plot(G, B, 'r.', label=r'Messwerte')
plt.plot(G, -1.01*G+0.02, label=r'fit')
plt.xlabel(r'G [1/mm]')
plt.ylabel(r'B [1/mm]')
plt.title(r"G-B Diagramm")
plt.legend()
plt.savefig('2.png')
plt.show()

c = ufloat(0.02,0.001)
print(1/c)

m = ufloat(50,2.5)
h = ufloat(50.369,0.7552)

print((h-m)/h)