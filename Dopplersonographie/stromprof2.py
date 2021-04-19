import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 

t, v6, v75 = np.genfromtxt('daten2.txt', unpack=True)



plt.plot(t, v75, 'r')

plt.xlabel(r'Messtiefe [µs]')
plt.ylabel(r'Strömungsgeschwindigkeit [L/min]')
plt.title(r"Strömungsprofil bei einer Pumpleistung von 7,5[L/min]")


plt.savefig('5.png')
plt.show()