import numpy as np 
import matplotlib.pyplot as plt 


x, y = np.genfromtxt('massendurchsatz.txt', unpack=True)
plt.plot(y, x, 'r.', label=r'$?$')


params, covariance_matrix = np.polyfit(y, x, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(0, 10)
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=2,
)

plt.xlim(0.00335, 0.00365)
plt.ylim(0.4, 1.8)
plt.xlabel(r'1/$T_2$ in (1/K)')
plt.ylabel(r'ln($p_b$)/$p_0$')

plt.savefig('massendurchsatz.png')
plt.show()