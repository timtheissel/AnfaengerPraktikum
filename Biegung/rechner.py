import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

lkee = ufloat(0.0510, 0.0016)
lbee = ufloat(0.0278, 0.0011)
lkre = ufloat(0.017, 0.0003)
lgre = ufloat(0.062, 0.0012)
lbebl = ufloat(0.0015, 0.00014)
lkebl = ufloat(0.0033, 0.00021)
lgrbl = ufloat(0.0097, 0.00015)
lkrbl = ufloat(0.0026, 0.00022)
lbebr = ufloat(0.0014, 0.00006)
lkebr = ufloat(0.0035, 0.00021)
lgrbr = ufloat(0.0096, 0.00034)
lkrbr = ufloat(0.0027, 0.00019)
i = (0.01**4)/12

ir = (np.pi*0.005**4)/4
#print(ir)
Ekee = (9.81*1.0543)/(2*i*lkee)
print(Ekee)

Ebee = (9.81*1.0543)/(2*i*lbee)
#print(Ebee)

Ekre = (9.81*0.2492)/(2*ir*lkre)
#print(Ekre)
Egre = (9.81*0.552)/(2*ir*lgre)
#print(Egre)


Ebebl = (9.81*2.3408)/(48*i*lbebl)
#print(Ebebl)

Ekebl = (9.81*2.3408)/(48*i*lkebl)
#print(Ekebl)

Egrbl = (9.81*2.3408)/(48*ir*lgrbl)
#print(Egrbl)

Ekrbl = (9.81*1.7294)/(48*ir*lkrbl)
#print(Ekrbl)

Ebebr = (9.81*2.3408)/(48*i*lbebr)
#print(Ebebr)

Ekebr = (9.81*2.3408)/(48*i*lkebr)
#print(Ekebr)

Egrbr = (9.81*2.3408)/(48*ir*lgrbr)
#print(Egrbr)

Ekrbr = (9.81*1.7294)/(48*ir*lkrbr)
#print(Ekrbr)

print((np.pi*0.005**2*0.602))