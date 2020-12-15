import numpy as np 
import matplotlib.pyplot as plt 

plt.title('Hall Effekt bei konstantem Spulenstrom von 5A')

x, y = np.genfromtxt('hall3.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$?$')

def sigmoid(x, a, b):
    return a*x+b

x, y = np.loadtxt('hall3.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, sigmoid(x, 0.0002, 0.00085))

plt.xlabel(r'Probenstrom (A)')
plt.ylabel(r'Hall Spannung (mV)')

plt.show()