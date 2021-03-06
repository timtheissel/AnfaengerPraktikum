import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

t, v6, v75 = np.genfromtxt('daten2.txt', unpack=True)



plt.plot(t, v6, 'r')

plt.xlabel(r'Messtiefe [µs]')
plt.ylabel(r'Strömungsgeschwindigkeit [L/min]')
plt.title(r"Strömungsprofil bei einer Pumpleistung von 6[L/min]")


plt.savefig('4.png')
plt.show()
