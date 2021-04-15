import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x = np.genfromtxt('1.txt', unpack=True)

y =sum(x)
print(y/7)