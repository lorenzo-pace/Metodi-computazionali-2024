import numpy as np
import matplotlib.pyplot as plt
import scipy 
import math
import argparse

l=[0.5, 1, 0.5]
alfa=[np.pi/4, np.pi/4, np.pi/30]
g=9.81
sol={}

def f(r, t, l):
    """
    Funzione Teta'' = -mg/l sin(teta)
    """
    dtetadt = r[1]
    dwdt = -g/l * np.sin(r[0])
    return (dtetadt, dwdt)

tt=np.linspace(0,10,1000)
yinit= np.empty((0,0))
for j in range(len(alfa)):
    yinit=(alfa[j], 0)
    print(yinit)
    yarr=scipy.integrate.odeint(f, yinit, tt, args=(l[j], ))
    sol.update({j : yarr})

plt.title('Pendolo', color='black', fontsize=14)
for j in range(len(alfa)):
    plt.plot(tt,sol[j][:,0])
plt.xlabel('t (s)')
plt.ylabel(r'$\theta$ (rad)')
plt.show()

