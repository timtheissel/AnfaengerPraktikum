import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit

x, es, ds = np.genfromtxt('Messwerte.txt', unpack=True)

D = 10e-9
L = 1.05
l = 633*10e-9
b = 0.15*10e-3
p = (x/100)/L

I1 = (es*1e-6)-10e-9
I2 = (ds*1e-6)-10e-9



def einzel(phi,b, a):
    lamda=633*10**(-9)
    uff=(a**2)*(b**2)*((lamda/(np.pi*b*(np.sin(phi)*180/np.pi)))**2)
    teil2=((np.sin((np.pi*b*np.sin(phi))/lamda)*180/np.pi))**2
    return(uff*teil2)

def doppel(phi,b,s):
    lamda=633*10**(-9)
    teil1=0.0003*np.cos((np.pi*s*np.sin(phi)/lamda))**2
    teil2=(lamda/(np.pi*b*np.sin(phi)))**2
    teil3=np.sin((np.pi*b*np.sin(phi))/lamda)**2
    return(teil1*teil2*teil3)



params, covariance =curve_fit(einzel,p,I1,p0=[0.00015,70])
errors = np.sqrt(np.diag(covariance))
print('breite des Spaltes:', params[0],'+-',errors[0])
#print('Abweichung', a(params[0],0.00015))
print('A_0:', params[1],'+-',errors[1])
#def einzel(phi,b,lamda,A_0)

params2, covariance2 =curve_fit(doppel,p,I2,p0=[0.00015, 0.00065])
errors2 = np.sqrt(np.diag(covariance2))
print('breite des Spaltes:', params2[0],'+-',errors2[0])
#print('Abweichung', a(params2[0],0.00015))
print('A_0:', params2[1],'+-',errors2[1])
#print(params2[2], '+-', errors2[2])

x2 = np.linspace(-0.2, 0.2, 50)


plt.figure()
plt.plot(p, (es*1e-6)-10e-9, 'rx', label=r'Messwerte')
plt.plot(x2, einzel(x2, 0.000146, 74.499), 'b-', label=r'fit')
plt.legend()
plt.xlabel('$ \phi \; [^\circ]$')
plt.ylabel('$ I-I_{Dunkel} \; [A]$')
plt.savefig('einzel.png')
plt.show()

plt.figure()
plt.plot(p, (ds*1e-6)-10e-9, 'rx', label=r'Messwerte')
plt.plot(x2, doppel(x2, 0.0001335, 0.00065), 'b-', label=r'fit')
plt.legend()
plt.xlabel('$ \phi \; [^\circ]$')
plt.ylabel('$ I-I_{Dunkel} \; [A]$')
plt.savefig('doppel.png')
plt.show()

plt.figure()
plt.plot(p, (es*1e-5)-10e-9, 'rx', label=r'Einzelspalt')
plt.plot(x2, einzel(x2, 0.000146, 235.499), 'r-', label=r'fit-Einzelspalt')
plt.plot(p, (ds*1e-6)-10e-9, 'bx', label=r'Doppelspalt')
plt.plot(x2, doppel(x2, 0.0001335, 0.00065), 'b-', label=r'fit-Doppelspalt')
plt.legend()
plt.xlabel('$ \phi \; [^\circ]$')
plt.ylabel(' (umskaliert)')
plt.savefig('vergleich.png')
plt.show()