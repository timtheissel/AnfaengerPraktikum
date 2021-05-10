import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

T = np.genfromtxt('ddruck.txt', unpack=True)

p = 5.5e7 * np.exp(-6876/T)
print(p)

w = (0.0029 / p) / 100
print(w)

v = 0.01 / w
print(v)

T1, T2 = np.genfromtxt('energiev.txt', unpack=True)

print(np.std(T1))
print(np.std(T2))

mT1 = ufloat(21.8, np.std(T1))
mT2 = ufloat(22.6, np.std(T2))

print(1/mT1)
print(1/mT2)

a= [23, 22, 22.5, 23, 22.5]
print(np.std(a))
b = ufloat(22.6, np.std(a) )

print(10/b)

e= [22, 23, 22.5, 23, 22.5]
print(np.std(e))
f = ufloat(22.6, np.std(e) )

print(10/f)

c = [4.84, 5.28, 5.06, 5.28, 5.28, 5.50, 5.28]
print(np.std(c))

g = [4.84, 5.06, 5.28, 4.84, 5.28, 5.50, 5.50]
print(np.std(g))

d= ufloat(5.22 , np.std(c))
print(d)

h= ufloat(5.18, np.std(g))


l = (4.136e-15 * 3e8)/d
print(l)

l1 = (4.136e-15 * 3e8)/4.9
print(l1)

l2 = (4.136e-15 * 3e8)/h
print(l)