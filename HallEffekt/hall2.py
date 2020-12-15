import numpy as np 
import matplotlib.pyplot as plt 

plt.title('Hall Effekt bei konstantem Probenstrom von 5A')

x, y = np.genfromtxt('hall2.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$?$')

def sigmoid(x, a, b):
    return a*x+b

x, y = np.loadtxt('hall2.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, sigmoid(x, 0.0015, 0.0037))

plt.xlabel(r'Spulenstrom (A)')
plt.ylabel(r'Hall Spannung (mV)')

plt.show()