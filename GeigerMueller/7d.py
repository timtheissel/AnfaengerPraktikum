import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 


U , I2, N2 = np.genfromtxt('Zaehlrohrstrom.dat', unpack=True)

N = unp.uarray(N2/60, np.ones(8)*np.sqrt(N2/60))
print(N)
I = unp.uarray(I2 * 1e-6, np.ones(8)*0.05 * 1e-6)
#print(I)
#print(const.e)
Z = I /(const.e * N)
print(Z)



plt.errorbar(U, unp.nominal_values(Z), yerr=unp.std_devs(Z), fmt='.')
plt.ylabel(r'Z')
plt.xlabel(r'Spannung [V]')
plt.title(r"Freigesetzte Ladungen pro einfallendem Teilchen")
plt.savefig('7d.png')

plt.show()
