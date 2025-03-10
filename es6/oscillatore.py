import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sys,os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcolo periodo oscillatore anarmonico.')
    parser.add_argument('--v6',    action='store_true', help='Potenziale V = kx^6')
    parser.add_argument('--v4',    action='store_true', help='Potenziale V = kx^4')
    parser.add_argument('--v2',    action='store_true', help='Potenziale V = kx^2')
    parser.add_argument('--v15',   action='store_true', help='Potenziale V = k|x|^3/2')
    parser.add_argument('--vall',  action='store_true', help='Confronto diversi potenziali')
    return  parser.parse_args()

m=1
k=0.1
vc=1
x0i = float(input('Inserire x0: '))
xx = np.arange(-5,5.1, 0.1)

def V6(x):
    return k*(x**6)
def Vp(x):
    return k*(x**0.5)
def V2(x):
    return k*(x**2)
def V4(x):
    return k*(x**4)
def V15(x):
    return k*(np.abs(x)**(1.5))

def integranda6 (x0, x):
   return 1/(np.sqrt(V6(x0)-V6(x)))
def integranda4 (x0, x):
   return 1/(np.sqrt(V4(x0)-V4(x)))
def integranda2 (x0, x):
   return 1/(np.sqrt(V2(x0)-V2(x)))
def integranda15 (x0, x):
   return 1/(np.sqrt(V15(x0)-V15(x)))

x1 = np.arange(0, x0i, (x0i)/100)
def T6(x0):
    t = np.sqrt(8*m)*integrate.simpson(integranda6(x0, x1), dx = 0.005)
    return t
def T4(x0):
    t = np.sqrt(8*m)*integrate.simpson(integranda4(x0, x1), dx = 0.005)
    return t
def T2(x0):
    t = np.sqrt(8*m)*integrate.simpson(integranda2(x0, x1), dx = 0.005)
    return t
def T15(x0):
    t = np.sqrt(8*m)*integrate.simpson(integranda15(x0, x1), dx = 0.005)
    return t

def grafico():
    ax = np.arange(0.1, 5, 0.1)
    ay = tempi
    plt.plot(ax,ay, color='orange')
    plt.xlabel('Posizione x0 (m)')
    plt.ylabel('Periodi (s)')
    plt.title('Periodo in funzione della posizione x0')
    plt.show()

Tarm = 2*np.pi *np.sqrt(m/k)

def oscillatore ():

    args = parse_arguments()

    #grafico()

    if args.v6 == True:
            fig,ax = plt.subplots(2,1, figsize=(10, 10) )

            tempi = np.empty(0)
            for x in np.arange(0.1, 5, 0.1):
                tempi = np.append(tempi, T6(x))
            print('Periodo corrispondente a x0= {x0i} con potenziale kx^6: T(x0) = ', T6(x0i))

            # subplot periodo
            ax[0].plot(xx, tempi,   color='magenta',   label='V(x)=c$x^6$')
            ax[0].axhline(Tarm, color='tomato',    label='$2 \pi \sqrt{2c/m}$')

            ax[0].legend(loc='upper center', fontsize=13)
            ax[0].set_xlabel(r'$x_0$ [m]')
            ax[0].set_ylabel(r'T [s]')
            ax[0].set_ylim(0, 14)

            # subplot energia potenziale
            xa = np.linspace(-1.15, 1.15, 100)

            ax[1].plot(xa, V6(xa, vc),   color='magenta',   label='V(x)=c$x^6$')

            ax[1].legend(fontsize=13)
            ax[1].set_xlabel(r'$x$ [m]')
            ax[1].set_ylabel(r'V [J]')

            plt.show()

    if args.v4 == True:
            fig,ax = plt.subplots(2,1, figsize=(10, 10) )

            tempi = np.empty(0)
            for x in np.arange(0.1, 5, 0.1):
                tempi = np.append(tempi, T4(x))
            print('Periodo corrispondente a x0= {x0i} con potenziale kx^4: T(x0) = ', T4(x0i))

            # subplot periodo
            ax[0].plot(xx, tempi,   color='magenta',   label='V(x)=c$x^4$')
            ax[0].axhline(Tarm, color='tomato',    label='$2 \pi \sqrt{2c/m}$')

            ax[0].legend(loc='upper center', fontsize=13)
            ax[0].set_xlabel(r'$x_0$ [m]')
            ax[0].set_ylabel(r'T [s]')
            ax[0].set_ylim(0, 14)

            # subplot energia potenziale
            xa = np.linspace(-1.15, 1.15, 100)

            ax[1].plot(xa, V4(xa, vc),   color='magenta',   label='V(x)=c$x^4$')

            ax[1].legend(fontsize=13)
            ax[1].set_xlabel(r'$x$ [m]')
            ax[1].set_ylabel(r'V [J]')

            plt.show()

    if args.v2 == True:
            fig,ax = plt.subplots(2,1, figsize=(10, 10) )

            tempi = np.empty(0)
            for x in np.arange(0.1, 5, 0.1):
                tempi = np.append(tempi, T2(x))
            print('Periodo corrispondente a x0= {x0i} con potenziale kx^2: T(x0) = ', T2(x0i))

            # subplot periodo
            ax[0].plot(xx, tempi,   color='magenta',   label='V(x)=c$x^2$')
            ax[0].axhline(Tarm, color='tomato',    label='$2 \pi \sqrt{2c/m}$')

            ax[0].legend(loc='upper center', fontsize=13)
            ax[0].set_xlabel(r'$x_0$ [m]')
            ax[0].set_ylabel(r'T [s]')
            ax[0].set_ylim(0, 14)

            # subplot energia potenziale
            xa = np.linspace(-1.15, 1.15, 100)

            ax[1].plot(xa, V2(xa, vc),   color='magenta',   label='V(x)=c$x^2$')

            ax[1].legend(fontsize=13)
            ax[1].set_xlabel(r'$x$ [m]')
            ax[1].set_ylabel(r'V [J]')

            plt.show()


    if args.vall == True:
            fig,ax = plt.subplots(2,1, figsize=(10, 10) )

            # subplot periodo
            ax[0].plot(xx, T15,  color='yellow', label='V(x)=c$|x|^{3/2}$')
            ax[0].plot(xx, T2,   color='green', label='V(x)=c$x^2$')
            ax[0].plot(xx, T4,   color='royalblue', label='V(x)=c$x^4$')
            ax[0].plot(xx, T6,   color='magenta',   label='V(x)=c$x^6$')
            ax[0].axhline(Tarm, color='tomato',    label='$2 \pi \sqrt{2c/m}$')

            ax[0].legend(loc='upper center', fontsize=13)
            ax[0].set_xlabel(r'$x_0$ [m]')
            ax[0].set_ylabel(r'T [s]')
            ax[0].set_ylim(0, 14)

            # subplot energia potenziale
            xa = np.linspace(-1.15, 1.15, 100)

            ax[1].plot(xa, V15(xa, vc),  color='yellow', label='V(x)=c$|x|^{3/2}$')
            ax[1].plot(xa, V2(xa, vc),   color='green', label='V(x)=c$x^2$')
            ax[1].plot(xa, V4(xa, vc),   color='royalblue', label='V(x)=c$x^4$')
            ax[1].plot(xa, V6(xa, vc),   color='magenta',   label='V(x)=c$x^6$')

            ax[1].legend(fontsize=13)
            ax[1].set_xlabel(r'$x$ [m]')
            ax[1].set_ylabel(r'V [J]')

            plt.show()

        



if __name__ == "__main__":

    oscillatore()