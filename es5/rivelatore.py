import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dati = [pd.read_csv(f'/home/loripace/MCF/es5/hit_times_M{i}.csv', sep=",") for i in range(4)]

# Istogramma dei tempi dei file.
for d in dati:
    plt.hist(d['hit_time'], bins = 50, color='red')
    plt.xlabel ('Hit times (ns)', fontsize =10)
    plt.show()

#Istogramma in scala logaritmica delle differenze dei tempi per i dati 0. 
delta = np.log10(np.ma.ediff1d(dati[0]['hit_time']))
plt.hist(delta, bins = 20, color='red')
plt.xlabel ('Hit times (ns)', fontsize =10)
plt.title('Istogramma in scala logaritmica delle differenze dei tempi [M0].')
plt.show()



# Coordinate centro Moduli [m]
xmod = [-5,  5, -5,  5]
ymod = [ 5,  5, -5, -5]
        
# Coordinate dei Sensori rispetto al centro del Modulo [m]
xdet = [-2.5, 2.5, 0, -2.5,  2.5]
ydet = [ 2.5, 2.5, 0, -2.5, -2.5]