import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 
R = ufloat(117.2,0.2)
L = ufloat(16.78,0.09)*10**-3
C = ufloat(2.066, 0.006)*10**-9

r = ((4*L)/C)
#print(r)

U = unp.sqrt(r)
#print(U)


v = R/L
#print(v)

p = unp.sqrt(L/(R**2*C))
print(p)