import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

x, y = np.genfromtxt('DatenGES5c.txt', unpack=True)
plt.plot(x, y, 'r.')
plt.xscale('log')
plt.show()