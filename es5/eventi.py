import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import reco

files = [f'/home/loripace/MCF/es5/hit_times_M{i}.csv' for i in range(4)]

#dati = [pd.read_csv(f'/home/loripace/MCF/es5/hit_times_M{i}.csv', sep=",") for i in range(4)]

def lettura(file_path):
    dati = pd.read_csv(file_path, header=None, names=['module_id', 'sensor_id', 'time'])
    dati['time'] = pd.to_numeric(dati['time'], errors='coerce')
    dati = dati.dropna()
    hits = [reco.Hit(c['module_id'], c['sensor_id'], c['time']) for _, c in dati.iterrows()]
    return hits

#Produca un array che corrisponda alla combinazione, 
#ordinata temporalmente, di tutti i reco.Hit

def raggruppa(hits, intervallo):
    hits.sort()  
    # ordinamento degli Hit in ordine di timestamp
    events = []
    current_event_hits = [hits[0]]

    for i in range(1, len(hits)):
        time_diff = hits[i] - hits[i - 1]
        if time_diff <= intervallo:
            current_event_hits.append(hits[i])
        else:
            events.append(reco.Evento(current_event_hits))
            current_event_hits = [hits[i]]
    
    # + ultimo evento
    if current_event_hits:
        events.append(reco.Evento(current_event_hits))
    
    return events

def elaboradati(file_paths):
    all_hits = []
    for file in file_paths:
        all_hits.extend(lettura(file))
    return all_hits

def creaevento(hits, t=500):
    return raggruppa(hits, t)

#finestra temporale in nanosecondi per separare gli eventi
intervallo = 10000

array_hits = []
for file in files:
    array_hits.extend(lettura(file))

eventi = raggruppa(array_hits, intervallo)

# Plot dei primi 10 eventi

for ev in eventi[:10]: 
    print(ev)

def istogrammi(events):
    numerohits = [ev.num_hits for ev in eventi]
    durate = [ev.duration for ev in eventi]
    deltat = np.diff([event.start_time for event in eventi])

    plt.hist(numerohits, bins=20, color='yellow', alpha=0.7)
    plt.xlabel("Numero di Hit per Evento")
    plt.ylabel("Conteggio")
    plt.title("Istogramma del numero di Hit per Evento")
    plt.show()

    plt.hist(durate, bins=20, color='green', alpha=0.7)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma della durata degli Eventi")
    plt.show()

    plt.hist(deltat, bins=20, color='red', alpha=0.7)
    plt.xlabel("Differenza di Tempo tra Eventi (ns)")
    plt.ylabel("Conteggio")
    plt.title("Istogramma delle differenze di tempo fra Eventi consecutivi")
    plt.show()

    # Grafico del numero di hit in funzione della durata
    plt.scatter(durate, numerohits, c='red', alpha=0.5)
    plt.xlabel("Durata dell'Evento (ns)")
    plt.ylabel("Numero di Hit")
    plt.title("Numero di Hit vs Durata dell'Evento")
    plt.show()

istogrammi(eventi)