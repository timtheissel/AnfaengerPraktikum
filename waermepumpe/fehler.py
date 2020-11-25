import numpy as np 
import matplotlib.pyplot as plt 


def sigmoid(t, a, b, c):
    return a*t**2+b*t +c

x, y = np.loadtxt('temperaturv.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid, x, y, p0=(24, 4, 1))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')


def sigmoid2(t, a, b, c):
    return a*t**2 + b*t + c

x, y = np.loadtxt('temperaturv2.txt', unpack=True)
from scipy.optimize import curve_fit
params, covariance_matrix = curve_fit(sigmoid2, x, y)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')