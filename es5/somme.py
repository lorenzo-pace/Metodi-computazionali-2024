import numpy as np
import sys

def somma(n):
    """
    Restituisce la somma dei primi *n* numeri naturali con *n* valore inserito dall'utente.
    """
    sum=0
    for j in range(n+1):
        sum = sum+j
        j+1
    return sum

def sommeradici(n):
    """
    Restituisce la somma delle radici dei primi *n* numeri naturali.
    """
    srad=0
    for j in range (n+1):
        srad+np.sqrt(j)
        j+1
    return srad

def sommaprodotto (n):
    """
    Restituisce ordinatamente somma e prodotto dei primi *n* numeri naturali. 
    """
    sum=0
    prod=1
    for j in range(n):
        sum = sum+(j+1)
        prod = prod*(j+1)
        j+1
    return sum, prod

def sommeinalfa (n, alfa=1):
    """
    Restituisce la somma dei primi *n* numeri naturali elevati al coefficiente *alfa* con valore di default 1.
    """
    suma=0
    for j in range(n):
        suma = suma+(j+1)**alfa
        j+1
    return suma


    
    
