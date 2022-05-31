import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

d = 0.04
l1 = 644e-9
n1 = 1.4567

D1 = l1*l1 / (2*d) * (1/(math.sqrt(n1*n1-1)))

print(D1)

n2 = 1.4635

l2 = 480e-9

D2 = l2*l2 / (2*d) * (1/(math.sqrt(n2*n2-1)))

print(D2)

L = 0.12

A1 = L/l1 * (n1*n1 - 1)

print(A1)

A2 = L/l2 * (n2*n2 - 1)

print(A2)

print(l1/D1)

print(l2/D2)