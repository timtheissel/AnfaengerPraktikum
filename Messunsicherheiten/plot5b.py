import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

L = ufloat(0.001678,0.00009)
C = ufloat(0.000000002066,0.00000000006)

R = ((4*L)/C)
print(R)

U = unp.sqrt(R)
print(U)
