import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x = [np.pi/12, np.pi/6, (np.pi)/3]

a = 90 - (np.arcsin(np.sin(x)*(1800/2700))*(180/np.pi))
print(a)

b =  (a * np.pi) / 180
print(b)

v, m1, m3, m6, d1, d3, d6, k1, k3, k6 = np.genfromtxt('daten.txt', unpack=True)

v0 = 2000000

vm = (2 * v0 * (m1/1800) * np.cos(b[0])) / 100 
print(vm)

vm3 = (2 * v0 * (m3/1800) * np.cos(b[1])) / 100 
print(vm3)

vm6 = (2 * v0 * (m6/1800) * np.cos(b[2])) / 100 
print(vm6)

vd = (2 * v0 * (d1/1800) * np.cos(b[0])) / 100 
print(vd)

vd3 = (2 * v0 * (d3/1800) * np.cos(b[1])) / 100 
print(vd3)

vd6 = (2 * v0 * (d6/1800) * np.cos(b[2])) / 100 
print(vd6)

vk = (2 * v0 * (k1/1800) * np.cos(b[0])) / 100 
print(vk)

vk3 = (2 * v0 * (k3/1800) * np.cos(b[1])) / 100 
print(vk3)

vk6 = (2 * v0 * (k6/1800) * np.cos(b[2])) / 100 
print(vk6)

ym1 = vm/(np.cos(b[0]))

plt.plot(v, ym1, 'r.', label=r'10mm Rohr')

yd1 = vd/(np.cos(b[0]))

plt.plot(v, yd1, 'b.', label=r'16mm Rohr')

yk1 = vk/(np.cos(b[0]))

plt.plot(v, yk1, 'g.', label=r'7mm Rohr')

plt.xlabel(r'Strömungsgeschwindigkeit [L/min]')
plt.ylabel(r'$\Delta \nu / \cos(\alpha)$ [Hz]')
plt.title(r"Dopplerwinkel 80.064$^{\circ}$")

plt.legend()
plt.show()
