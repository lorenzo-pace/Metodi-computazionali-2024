import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#esercitazione 3 21 ottobre 2024

dati = pd.read_csv('kplr010666592-2011240104155_slc.csv')
print("2. Colonne usate: ", dati['TIME'], dati['PDCSAP_FLUX'], dati['PDCSAP_FLUX_ERR'])

#3. grafico del flusso in funzione del tempo

y1=dati['PDCSAP_FLUX']
x1=dati['TIME']

plt.plot(x1, y1, color='limegreen', label='Y1' )

plt.xlabel('Tempi')
plt.ylabel('Flusso')
plt.legend()
plt.show()

#4. flusso su tempo coi punti del grafico demarcati da un simbolo (no linea)

plt.plot(x1, y1, 'o', color='limegreen', label='Y1' )

plt.xlabel('Tempi')
plt.ylabel('Flusso')
plt.legend()
plt.show()

#5. grafico del flusso su tempo con barre di errore e salva pdf

y1err = dati['PDCSAP_FLUX_ERR']
plt.errorbar(x1, y1, yerr=y1err, fmt= 'o')
plt.title('Grafico flusso su tempo con errori. ')
plt.xlabel('Tempi')
plt.ylabel('Flusso')
plt.show()
plt.savefig("Grafico1.pdf")

#6. grafico selezionando un intervallo temporale attorno ad uno dei minimi

minimo = min(dati['PDCSAP_FLUX'])
datilim = dati.loc[( dati['PDCSAP_FLUX']< minimo-1) & ( dati['PDCSAP_FLUX'] < minimo +1)]
plt.errorbar(datilim['TIME'], datilim['PDCSAP_FLUX'], fmt= 'o')
plt.title('Grafico limitato intorno a un minimo di flusso su tempo con errori. ')
plt.xlabel('Tempi, t in un intorno verticale di raggio 1 del minimo')
plt.ylabel('Flusso')
plt.show()

#7. selezione del punto 6 mostrata come riquadro

fig,ax = plt.subplots(1,2, figsize=(12,6) )

ax[0].plot(x1, y1, 's-', color='yellow')
ax[1].plot(datilim['TIME'], datilim['PDCSAP_FLUX'], '*',  color='red'  )

ax[0].set_title('Grafico intero', fontsize=15, color='black')
ax[1].set_title('Grafico limitato', fontsize=15, color='black')

ax[0].set_ylabel('Flusso')
ax[0].set_xlabel('Tempo')

ax[1].set_xlabel('Tempo')
ax[1].set_ylabel('Flusso')

ax[0].tick_params(axis='x', labelsize=14)
ax[0].tick_params(axis='y', labelsize=14)
ax[0].grid(True)

plt.show()
