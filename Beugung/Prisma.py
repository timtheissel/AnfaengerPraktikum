import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

a1, r2, g2 = np.genfromtxt('Prisma.txt', unpack=True)

n = ufloat(1.494, 0.019)

a = (a1 * np.pi)/ 180
r = (r2 * np.pi)/ 180 
g = (g2 * np.pi)/ 180 

b1 = (unp.arcsin(np.sin(a)/n))*180/np.pi 
print(b1)

b2 = 60 - b1
print(b2)

D = (a1+r2)-(b1+b2)
print(D)

D2 = (a1+g2)-(b1+b2)
print(D2)

