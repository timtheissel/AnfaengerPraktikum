import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

s = unp.uarray([75, 57, 52, 42, 35, 32, 30], [5])

s2 = unp.uarray([150, 115, 105, 85, 70, 65, 60], [5])

S = unp.uarray([275, 220, 190, 175, 160, 150, 135], [5])

d = 0.04
l1 = 480e-9
n1 = 1.4635

D1 = l1*l1 / (2*d) * (1/(math.sqrt(n1*n1-1)))

dl = 1/2 * s/S *D1

dl2 = 1/2 * s2/S *D1

print(dl)

print(dl2)

m = 9.274e-24
c = 3e8
h = 6.626e-34

dE = h * c / (480e-9)**2 * 6.59e-12

print(dE)

print(dE / (0.369466 * m))

print(np.mean(dl2))