import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#esercitazione 3 21 ottobre 2024 secondo esercizio
dati = pd.read_csv('ExoplanetsPars_2024.csv', comment='#')

print(dati.columns)
#stampo solo un pezzo di dataframe (colonne a caso)
print(dati['st_mass'])

#grafico con assi logaritmici della massa del pianeta sul periodo orbitale


plt.scatter( dati['pl_orbper'], dati['st_mass'], color='royalblue', s=20)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.ylim(0, 100)
plt.title('Grafico logaritmico massa pianeta contro periodo orbitale')
plt.legend(fontsize=14)
plt.show()

#grafico con assi logaritmici del quadrato del semiasse maggiore contro la massa

ordinate = (dati['pl_orbsmax']**2)/dati['st_mass']

plt.scatter( ordinate, dati['pl_orbper'], color='red', s=15)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.ylim(0, 100)
plt.title('Grafico logaritmico R^2/m contro il periodo orbitale')
plt.legend(fontsize=14)
plt.show()

#grafico con assi logaritmici della massa del pianeta sul periodo orbitale


plt.scatter( dati['pl_orbper'], dati['st_mass'], color='royalblue', s=20)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.ylim(0, 100)
plt.title('Grafico logaritmico massa pianeta contro periodo orbitale')
plt.legend(fontsize=14)

plt.show()

#grafico con assi logaritmici della massa del pianeta sul periodo orbitale

bytransit = dati.loc[dati['discoverymethod']=='Transit']
byradvel = dati.loc[dati['discoverymethod']=='Radial Velocity']

plt.scatter( byradvel['pl_orbper'], byradvel['st_mass'], color='red', alpha=0.4, s=20, label='Scoperti tramite Radial Velocity')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.ylim(0, 100)
plt.title('Grafico logaritmico massa pianeta contro periodo orbitale')
plt.legend(fontsize=14)

plt.scatter( bytransit['pl_orbper'], bytransit['st_mass'], color='yellow', alpha=0.4, s=20, label='Scoperti tramite Transit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.ylim(0, 100)
plt.title('Grafico logaritmico massa pianeta contro periodo orbitale')
plt.legend(fontsize=14)

plt.show()

