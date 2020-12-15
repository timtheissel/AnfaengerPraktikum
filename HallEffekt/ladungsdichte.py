import numpy as np 
import matplotlib.pyplot as plt 


plt.title('Magnetfeldstärke bei veränderter Stromstärke')

x, y = np.genfromtxt('ladungsdichte.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$?$')

def sigmoid(x, a, b):
    return a*x+b

x, y = np.loadtxt('ladungsdichte.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, sigmoid(x, 135.425, 2.719))

plt.xlabel(r'Spulenstromstärke (A)')
plt.ylabel(r'Magnetfeldstärke (mT)')

plt.savefig('Mangnetfeld.png')
plt.show()