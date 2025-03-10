import numpy as np
import matplotlib.pyplot as plt
import math

class Hit:
    def _init_(self, mid, sid, time):

        self.mid = mid  
        self.sid = sid
        self.time = time
    def _eq_(self, a):
        return self.time == a.time
    def _lt_(self, a):
        if self.time == a.time:
            return 10*self.mid + self.sid < 10*a.mid + a.sid
        else:
            return self.time < a.time
    def _gt_(self, a):
        return self.time > a.time
    def _add_(self, a):
        return self.time + a.time
    def _sub_(self, a):
        return self.time - a.time

#Numero di Hit
#Time Stamp del primo Hit
#Time Stamp dell'ultimo Hit
#Durata temporale
#Array di tutti gli Hit

class Evento:
    def __init__(self, hits):
        self.hits = hits 
        self.start_time = hits[0].timestamp if hits else None
        self.end_time = hits[-1].timestamp if hits else None
        self.duration = self.end_time - self.start_time if self.start_time and self.end_time else 0
        self.num_hits = len(hits)

    def __repr__(self):
        return (f"Numero di hit: = {self.num_hits}, "
                f"Time stamp del primo hit: ={self.start_time}, "
                f"Time stamp dell'ultimo hit: ={self.end_time}, "
                f"Durata: = {self.duration})")
