import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

M1 = ufloat(96041,309.9048)
M = ufloat(158479, 398.0942)
M2 = ufloat(76518,276.6189)

N1 = M1/120
N = M/120
N2 = M2/120
print(N1)
print(N)
print(N2)
T = (N1+N2-N)/(2*N1*N2)
print(T)

