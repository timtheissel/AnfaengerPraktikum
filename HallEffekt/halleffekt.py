import numpy as np 
import matplotlib.pyplot as plt 

plt.title('Hall Effekt bei konstantem Probenstrom von 5A')

x, y = np.genfromtxt('hall.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$?$')

def sigmoid(x, a, b):
    return a*x+b

#x, y = np.loadtxt('hall.txt', unpack=True)
#from scipy.optimize import curve_fit
#params, covariance_matrix = curve_fit(sigmoid, x, y)
#
#uncertainties = np.sqrt(np.diag(covariance_matrix))
#
#for name, value, uncertainty in zip('abc', params, uncertainties): 
#    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.subplot(2, 2, 1)
plt.plot(x, sigmoid(x, 0.002, 0.008))
plt.plot(x,y, 'r.')
plt.xlabel(r'Spulenstrom (A)')
plt.ylabel(r'Hall Spannung (mV)')

plt.subplot(2, 2, 2)
b, v = np.genfromtxt('hall2.txt', unpack=True)
plt.plot(b, sigmoid(b, 0.0015, 0.0037))
plt.plot(b, v, 'r.')
plt.xlabel(r'Spulenstrom (A)')
plt.ylabel(r'Hall Spannung (mV)')

plt.subplot(2, 2, 3)
l, k = np.genfromtxt('hall3.txt', unpack=True)
plt.plot(l, sigmoid(l, 0.0002, 0.00085))
plt.plot(l, k, 'r.')


plt.xlabel(r'Probenstrom (A)')
plt.ylabel(r'Hall Spannung (mV)')

plt.tight_layout()

plt.savefig('plothall.png')
plt.show()
