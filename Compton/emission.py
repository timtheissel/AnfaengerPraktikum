import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

t, I = np.genfromtxt('EmissionCu.dat', unpack=True)

k_a = ufloat(22.5, 0.2)
k_b = ufloat(20.2, 0.2)

plt.plot(t, I, 'r.', label=r'Daten')
plt.scatter([11.1], [420.0], s=20, marker='o', color='blue')
plt.annotate(r'Bremsberg', 
            xy = (11.1, 420.0), xycoords='data', xytext=(-60, 20),
            textcoords='offset points', fontsize=12, 
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-.2"))
plt.scatter([k_b.n], [1599.0], s=20, marker='o', color='blue')
plt.annotate(r'$K_{\beta}$',
            xy = (k_b.n, 1599.0), xycoords='data', xytext=(50, 25),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.scatter([k_a.n], [5050.0], s=20, marker='o', color='blue')
plt.annotate(r'$K_{\alpha}$',
            xy = (k_a.n, 5050.0), xycoords='data', xytext=(-40, -20),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

plt.ylabel(r'Impulse [1/s]')
plt.xlabel(r'Einfallswinkel $\theta$ [$^\circ$]')
plt.title(r"Bestimmung der Kennlinien")
plt.legend()
plt.savefig('a1.png')
#plt.show()

d = 2.014e-10
p = 4.136e-15
c = 3e8
Ea = 8046
Eb = 8903

a = 2*d*unp.sin(((k_a)*np.pi)/180)
print(a)
b = 2*d*unp.sin(((k_b)*np.pi)/180)
print(b)


print((p*c)/a)
print((p*c)/b)
print((p*c)/Ea)
print((p*c)/Eb)
