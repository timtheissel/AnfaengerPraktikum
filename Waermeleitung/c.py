import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('c.dat', unpack=True)

plt.figure()
plt.plot(x/2, T7, label=r'T7')
plt.plot(x/2, T8, label=r'T8')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('T [$^\circ$C]')
plt.title('Temperaturverlauf von T7 und T8')
plt.savefig('steel.png')
plt.show()



k = [262.80, 181.80, 260.78, 164.43, 249.84, 222.31, 283.85, 246.60, 254.70, 262.80]

print(np.std(k))

k2 = [142.88,
200.03,
153.43,
169.64,
160.96,
148.36,
178.32,
163.56,
195.70,
202.63,]

print(np.std(k2))

t = 80
t2 = 200

w = 2* np.pi / t 
w2 = 2* np.pi / t2

pb = 8.73
pa = 2.7

kb = ufloat(171.51, 20.67)
ka= ufloat(238.99, 36.27)

print((200-ka)/200)
print((120-kb)/120)
