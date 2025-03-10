import numpy as np
import matplotlib.pyplot as plt
import scipy 
import math
import argparse

RC = [0.25, 1, 4]
a = 0
b = 10
v0=0
n=500

#dizionari per le soluzioni
vout_sol={}
t_sol={}

def vin(t):
    """
    Definizione del potenziale Vin secondo la maschera pari/dispari.
    """
    if np.isscalar(t):
        if int(t)%2 == 0:
            return 1
        else:
            return -1
    else:
        v = np.ones(len(t)) 
        odd_mask = t.astype(int)%2 != 0
        v[odd_mask] = -1
        return v

def f(Vout, t, k):
    """
    Funzione dVout/dt(x) = 1/RC*(Vin-Vout)
    """
    return 1/k*(vin(t)-Vout)

h = (b-a)/n
tt = np.arange(a,b,h)
vout = np.empty(0)

for rc in RC:
    vout = scipy.integrate.odeint(f, y0=v0, t=tt, args = (rc,))
    vout_sol.update({rc : vout})
    t_sol.update({rc : tt})

fig,ax = plt.subplots(1,3, figsize=(9,6))
plt.title('Risoluzione equazione differenziale del filtro passa-basso', color='black', fontsize=14)
for jrc, jind in zip(RC, range(len(RC))):
    ax[jind].plot(tt,vout_sol[jrc])
    ax[jind].set_xlabel('t (s)')
    ax[jind].set_ylabel('V_out (V)')
    ax[jind].set_title(f"RC = {jrc} s")
#plt.text(1, -30, r'$\frac{dV_{out}}{dt} = \frac{1}{RC} (V_{in}-V_{out})$', color='slategray',fontsize=14)
plt.show()
