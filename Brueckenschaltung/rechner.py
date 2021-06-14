import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

R2 = ufloat(664, 0.002*664)
R3 = 263
R4 = 737

R34 = ufloat(R3/R4, 0.005*(R3/R4))

R = R2*R34
print(R)

R2 = ufloat(1000, 0.002*1000)
R3 = 192.5
R4 = 807.5

R34 = ufloat(R3/R4, 0.005*(R3/R4))

R = R2*R34
print(R)

R2 = ufloat(269, 0.03*269)
R3 = 630
R4 = 370
C2 = ufloat(750, 0.002*750)
print(R2*(R3/R4))
print(C2*(R4/R3))

R2 = ufloat(228, 0.03*228)
R3 = 592
R4 = 408
C2 = ufloat(20.1, 0.002*20.1)
print(R2*(R3/R4))
print(C2*(R3/R4))

R2 = ufloat(1000, 1000*0.002)
R3 = ufloat(73, 0.03*73)
R4 = ufloat(192, 0.03*192)
C4 = ufloat(750, 750*0.002)
print(R2 * (R3/R4))
print(R2*R3*C4)

f, U = np.genfromtxt('e.txt', unpack=True)
l= np.linspace(20,20000,20000)
Us = 10
f0 = 540
v = f/f0
v2 = l/f0
a = (v2**2-1)**2
b = (1-v2**2)**2



plt.plot(v, U/Us, 'r.', label=r'Messwerte')
plt.plot(v2, np.sqrt(1/9*a*(1/(b+9*v2**2))), label=r'Theoriekurve')
plt.xscale('log')
plt.xlabel('v/v$_0$')
plt.ylabel('U$_{Br}$(v)/U$_S$(v)')
plt.title('Frequenzabhängigkeit der Brückenspannung einer Wien-Robinson-Brücke')
plt.legend()
plt.savefig('e.png')
plt.show()


print(0.01/np.sqrt(9/(9*(9+9*4))))