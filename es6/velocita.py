import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sys,os
import argparse


dati = pd.read_csv('vel_vs_time.csv')
tempi = dati['t'].values
vel = dati['v'].values

#grafico della velocità in funzione del tempo
def grafvel ():
    ax = tempi
    ay = vel
    plt.plot(ax,ay, color='limegreen')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocità (m/s)')
    plt.title('1. Velocità in funzione del tempo')
    plt.show()

#distanze calcolate con l'integrale alla Simpson
dist = np.empty(0)
for j in range(len(vel)):
    dist = np.append(dist, integrate.simpson(vel[:j+1], dx= tempi[1]-tempi[0]))

#grafico della distanza in funzione del tempo
def grafdist ():
    ax = tempi
    ay1 = dist
    plt.plot(ax,ay1, color='royalblue')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Distanza (m)')
    plt.title('2. Distanza in funzione del tempo')
    plt.show()

#grafvel()
#grafdist()

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('-v', '--velocita',    action='store_true',                     help='Grafico velocita su tempo')
    parser.add_argument('-d', '--distanze',    action='store_true',                     help='Grafico distanze su tempo')
    parser.add_argument('-f', '--file',        action='store_true',                     help='Esempio di opzione con valore tipo e default')
    return  parser.parse_args()

def main():

    args = parse_arguments()

    # print 
    #print(args)

    if args.velocita == True:
        grafvel()

    if args.distanze == True:
        grafdist()

    if args.file == True:
        dati = pd.read_csv('vel_vs_time.csv')
        print(dati)


if __name__ == "__main__":

    main()