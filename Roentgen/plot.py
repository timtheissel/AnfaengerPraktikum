import math
import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties as unc 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
import scipy.constants as const

h = const.h
c = const.c 
e = const.e
d = 201.4e-12
E_abs = 8980.476
R = 13.6 

theta, N = np.genfromtxt('bragg.txt', unpack=True)

plt.figure(1)
plt.plot(theta, N, 'rx', label=r'Messwerte')
plt.vlines(x=28.2, ymin=50, ymax=225, label=r'Maximum')
plt.legend()
plt.xlabel('$ \Theta [^\circ]$')
plt.ylabel('[Imp/s]')
plt.savefig('bragg.png')
#plt.show()

th, N2 = np.genfromtxt('emissionsspektrum.txt', unpack=True)

k_a = ufloat(22.5, 0.2)
k_b = ufloat(20.2, 0.2)

plt.figure(2)
plt.plot(th, N2, 'rx', label=r'Messwerte')
plt.vlines(x=20.2, ymin=50, ymax=5155, label=r'K$_\beta$', linestyles ="dashed", colors ="g")
plt.vlines(x=22.5, ymin=50, ymax=5155, label=r'K$_\alpha$', linestyles ="dashed", colors ="b")
plt.hlines(y=1599/2, xmin=20.1, xmax=20.6, label=r'FWHM K$_\beta$', colors ="y")
plt.hlines(y=5050/2, xmin=22.3, xmax=22.9, label=r'FHWM K$_\alpha$', colors ="salmon")
plt.scatter([11.1], [420.0], s=20, marker='o', color='blue')
plt.annotate(r'Bremsberg', 
            xy = (11.1, 420.0), xycoords='data', xytext=(-60, 20),
            textcoords='offset points', fontsize=12, 
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-.2"))
plt.scatter([k_b.n], [1599.0], s=20, marker='o', color='blue')
plt.annotate(r'$K_{\beta}$',
            xy = (k_b.n, 1599.0), xycoords='data', xytext=(50, 25),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.scatter([k_a.n], [5050.0], s=20, marker='o', color='blue')
plt.annotate(r'$K_{\alpha}$',
            xy = (k_a.n, 5050.0), xycoords='data', xytext=(-40, -20),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

plt.ylabel(r' [Impulse/s]')
plt.xlabel(r'Einfallswinkel $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('copper.png')
#plt.show()


def E(th): #In eV
    return h * c / (2 * d * unp.sin(th * np.pi /180 ) * e)

b_l = ufloat(20.2 , 0.2)
b_r = ufloat(20.6 , 0.2)
a_l = ufloat(22.4 , 0.2)
a_r = ufloat(22.9 , 0.2)

dE_a = E(a_l) - E(a_r)
print("Delta E_a", E(a_l) - E(a_r) )
dE_b = E(b_l) - E(b_r)
print("Delta E_b", E(b_l) - E(b_r) )

E_max_a = E(k_a)
print("E,max alpha" , E_max_a)
E_max_b = E(k_b)
print("E,max beta"  , E_max_b)

A_a = E_max_a / dE_a
A_b = E_max_b / dE_b
print("Auflösung Peak alpha: " , A_a)
print("Auflösung Peak beta: " , A_b)

print('Absorptionskoeffizienten')
s1 = 29 - unp.sqrt(E_abs/R)
print("s1: " , s1)
s2 = 29 - 2* unp.sqrt((E_abs - E(k_a))/R)
print("s2: " , s2)
s3 = 29 - 3* unp.sqrt((E_abs - E(k_b))/R)
print("s3: " , s3)


th_br, N_br = np.genfromtxt('brom.txt', unpack=True)
th_ga, N_ga = np.genfromtxt('gallium.txt', unpack=True)
th_rb, N_rb = np.genfromtxt('rubidium.txt', unpack=True)
th_sr, N_sr = np.genfromtxt('strontium.txt', unpack=True)
th_zn, N_zn = np.genfromtxt('zink.txt', unpack=True)
th_zr, N_zr = np.genfromtxt('zirkonium.txt', unpack=True)

def sigmoid(x, a, b):
    return a*x+b 

plt.figure(3)
plt.plot(th_br, N_br, 'rx', label=r'Messwerte')
plt.plot(np.linspace(13.1, 13.3, 50), sigmoid(np.linspace(13.1, 13.3, 50), 40, -511), label=r'Hilfsgerade')
plt.plot(13.225, 18, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('br.png')

plt.figure(4)
plt.plot(th_ga, N_ga, 'rx', label=r'Messwerte')
plt.plot(np.linspace(17.3, 17.4, 50), sigmoid(np.linspace(17.3, 17.4, 50), 140, -2334), label=r'Hilfsgerade')
plt.plot(17.34, 94, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('ga.png')

plt.figure(5)
plt.plot(th_rb, N_rb, 'rx', label=r'Messwerte')
plt.plot(np.linspace(11.7, 11.8, 50), sigmoid(np.linspace(11.7, 11.8, 50), 70, -787), label=r'Hilfsgerade')
plt.plot(11.77, 37, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('rb.png')


plt.figure(6)
plt.plot(th_sr, N_sr, 'rx', label=r'Messwerte')
plt.plot(np.linspace(11.0, 11.1, 50), sigmoid(np.linspace(11.0, 11.1, 50), 310, -3321), label=r'Hilfsgerade')
plt.plot(11.09, 118, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('sr.png')



plt.figure(7)
plt.plot(th_zn, N_zn, 'rx', label=r'Messwerte')
plt.plot(np.linspace(18.6, 18.7, 50), sigmoid(np.linspace(18.6, 18.7, 50), 190, -3469), label=r'Hilfsgerade')
plt.plot(18.67, 78, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('zn.png')


plt.figure(8)
plt.plot(th_zr, N_zr, 'rx', label=r'Messwerte')
plt.plot(np.linspace(9.9, 10.0, 50), sigmoid(np.linspace(9.9, 10.0, 50), 450, -4275), label=r'Hilfsgerade')
plt.plot(9.96, 206.5, 'go', label=r'I$_K$')
plt.ylabel(r' [Impulse/s]')
plt.xlabel(r' $\theta$ [$^\circ$]')
plt.legend()
plt.savefig('zr.png')


print('minbrom', np.min(N_br))
print('maxbrom', np.max(N_br))
print('minga', np.min(N_ga))
print('maxga', np.max(N_ga))
print('minrb', np.min(N_rb))
print('maxrb', np.max(N_rb))
print('minsr', np.min(N_sr))
print('maxsr', np.max(N_sr))
print('minzn', np.min(N_zn))
print('maxzn', np.max(N_zn))
print('minzr', np.min(N_zr))
print('maxzr', np.max(N_zr))

print('IKbr', np.min(N_br)+((np.max(N_br)-np.min(N_br))/2))
print('IKga', np.min(N_ga)+((np.max(N_ga)-np.min(N_ga))/2))
print('IKrb', np.min(N_rb)+((np.max(N_rb)-np.min(N_rb))/2))
print('IKsr', np.min(N_sr)+((np.max(N_sr)-np.min(N_sr))/2))
print('IKzn', np.min(N_zn)+((np.max(N_zn)-np.min(N_zn))/2))
print('IKzr', np.min(N_zr)+((np.max(N_zr)-np.min(N_zr))/2))


x_br = [13.1, 13.3]
y_br = [13.0, 21]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_br, y_br)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xikbr = (18+511)/40
print(xikbr)

x_ga = [17.3, 17.4]
y_ga = [88, 102]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_ga, y_ga)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xikga = (94+2334)/140
print(xikga)

x_rb = [11.7, 11.8]
y_rb = [32, 39]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_rb, y_rb)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xikrb = (37+787)/70
print(xikrb)

x_sr = [11, 11.1]
y_sr = [89, 120]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_sr, y_sr)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xiksr = (118+3321)/310
print(xiksr)

x_zn = [18.6, 18.7]
y_zn = [65, 84]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_zn, y_zn)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xikzn = (78+3469)/190
print(xikzn)

x_zr = [9.9, 10]
y_zr = [180, 225]

from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x_zr, y_zr)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

xikzr = (206.5+4275)/450
print(xikzr)

print(E(xikbr))
print(E(xikga))
print(E(xikrb))
print(E(xiksr))
print(E(xikzn))
print(E(xikzr))



w = (E(xikbr))/(R) - (const.alpha**2 * 35**4)/(4)
print(35-np.sqrt(w))

w = (E(xikga))/(R) - (const.alpha**2 * 31**4)/(4)
print(31-np.sqrt(w))

w = (E(xikrb))/(R) - (const.alpha**2 * 37**4)/(4)
print(37-np.sqrt(w))

w = (E(xiksr))/(R) - (const.alpha**2 * 38**4)/(4)
print(38-np.sqrt(w))

w = (E(xikzn))/(R) - (const.alpha**2 * 30**4)/(4)
print(30-np.sqrt(w))

w = (E(xikzr))/(R) - (const.alpha**2 * 40**4)/(4)
print(40-np.sqrt(w))

E = [
E(xikbr),
E(xikga),
E(xikrb),
E(xiksr),
E(xikzn),
E(xikzr),
]

z = [35, 31, 37, 38, 30, 40]

asf = np.linspace(90, 140, 50)

plt.figure(9)
plt.plot(np.sqrt(E), z, 'rx', label=r'$\sqrt{E_{abs}}$')
plt.plot(asf, sigmoid(asf, 0.283, 2.277), label=r'Ausgleichsgerade')
plt.ylabel(r' Ordnungszahlen Z')
plt.xlabel(r' ')
plt.legend()
plt.savefig('ryd.png')

a = ufloat(0.283, 0.01)

R = 1/(a**2)
print(R)


from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, np.sqrt(E), z)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')