import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

a, b = np.genfromtxt('rechner.txt', unpack=True)

a1 = (a * np.pi)/ 180
b1 = (b * np.pi)/ 180 

n= np.sin(a1)/np.sin(b1)
print(n)
print(np.std(n))

n1 = ufloat(1.494, 0.019)

print(299792458/n1)

d = 5.85 

s = (d * np.sin(a1-b1))/np.cos(b1) 
print(s)

b2 = unp.arcsin(np.sin(b1)/n1)
print(b2/np.pi * 180)

s1 = (d * unp.sin(a1-b2))/unp.cos(b2) 
print(s1)