import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

t, v6, v75 = np.genfromtxt('daten2.txt', unpack=True)

fig, axs = plt.subplots(2)
axs[0].plot(t, v6)
axs[1].plot(t, v75)





plt.show()
