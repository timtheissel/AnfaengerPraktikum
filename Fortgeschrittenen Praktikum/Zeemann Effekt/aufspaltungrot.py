import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

s = unp.uarray([110, 77, 60, 55, 50], [5])

S = unp.uarray([365, 290, 245, 220, 190], [5])

d = 0.04
l1 = 644e-9
n1 = 1.4567

D1 = l1*l1 / (2*d) * (1/(math.sqrt(n1*n1-1)))

dl = 1/2 * s/S *D1

print(dl)

m = 9.274e-24
c = 3e8
h = 6.626e-34

dE = h * c / (644e-9)**2 * 6.48e-12

print(dE)

print(dE / (0.564573 * m))

print(np.mean(dl))
