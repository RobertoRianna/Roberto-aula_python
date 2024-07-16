#somma e media degli elementi
import numpy as np

def crea():
    array = np.random.randint(1, 101,15)                #creazione di 15 numeri casuali che vanno da 1 a 100
    print(array)

def somma(array):
    somma_array = np.sum(array)                         #somma dell'array
    print(somma_array)

def media(array):
    media_array = np.mean(array)                        #media dell'array
    print(media_array)
