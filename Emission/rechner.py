import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as cons


I, U  = np.genfromtxt('rechner.txt', unpack=True)

f = 0.35
s = 5.7e-12
e = 0.28
N = ufloat(0.95, 0.05)


T = ((I*U-N)/(f*s*e))**0.25
print(T)

m = 9.109e-31
e = 1.602e-19
k = 1.380e-23
h = 6.626e-34

A = (4*np.pi*e*m*k**2)/(h**3)
print(A)

B =A*T**2
print(B)

C = I/B
print(C)

D = unp.log(C)
print(D)

E = D*k*T
print(E)

F = E/-e
print(F)