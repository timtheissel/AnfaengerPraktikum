import numpy as np 
import matplotlib.pyplot as plt 




plt.title('Temperaturverläufe')



#def sigmoid(t):
 #   return -0.012*t**2 + 1.217*t + 21.820

def sigmoid(t):
    return  -0.00000347*t**2 + 0.0209*t + 294.54

plt.plot(np.linspace(0, 2100, 5000), sigmoid(np.linspace(0, 2100, 5000)), color='black', label="Ausgleichsgerade $T_1$")


#plt.plot(np.linspace(0, 35, 1000), sigmoid(np.linspace(0, 35, 1000)), color='black', label="Ausgleichsgerade $T_1$")



def sigmoid2(t):
    return 0.0000009563*t**2 + -0.0111*t + 295.88


plt.plot(np.linspace(0, 2100, 5000), sigmoid2(np.linspace(0, 2100, 5000)), color='black', label="Ausgleichsgerade $T_2$")

x, y = np.genfromtxt('temperaturv2.txt', unpack=True)
plt.plot(x, y, 'b.', label=r'$T_2$')


x, y = np.genfromtxt('temperaturv.txt', unpack=True)
plt.plot(x, y, 'r.', label=r'$T_1$')
plt.xlabel(r'Zeit t (s)')
plt.ylabel(r'Temperatur (°K)')

plt.legend()
plt.savefig('plot2.png')
plt.show()