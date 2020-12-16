import math
import numpy as np 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const 


#ufloat.n =Wert, ufloat.s = Fehler
#ufloat(Wert, Fehler)
#unp.uarray([werte][Fehler])
#unp.nominal_values(nameUarray
#unp.std_devs(NameArray)


Ip, Tp, Up, Im, Tm, Um = np.genfromtxt('ladungsdichte_rechner_daten.txt', unpack=True)

d = ufloat(1.8e-8,1.8e-11)

n= -(Ip*Tp)/(Up*d*const.e)
n2= -(Im*Tm)/(Um*d*const.e)
#print(n)
#print(n2)


rho = 8.96
#print(rho)
ml = 63.546e-3
#print(ml)
Z = (n*ml)/(rho*const.N_A)
Z2 = (n2*ml)/(rho*const.N_A)
#print(Z)
#print(Z2)

tau = (2*const.m_e)/(n*const.e**2*rho)
#print(tau)

j=1
vd = (-n*const.e)/j
#print(vd)

mu = -(const.e*tau)/(2*const.m_e)
print(mu)

EF=const.h*(3/(8*math.pi)**(1/3))/(2*const.m_e)
#print(EF)

v = ((2*EF)/const.m_e)
#print(v)

l = -tau * v
print(l)