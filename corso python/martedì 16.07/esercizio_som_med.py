#somma e media degli elementi
import numpy as np

def crea():
    array = np.random.randint(1, 101,15)                #creazione di 15 numeri casuali che vanno da 1 a 100
    return array

def somma(array):
    somma_array = np.sum(array)                         #somma dell'array
    return somma_array

def media(array):
    media_array = np.mean(array)                        #media dell'array
    return media_array


def menù():
    controllo = True
    while True:
        print("Menù")
        print("Crea array (1) ")
        print("somma array (2) ")
        print("Media array (3) ")
        print("Exit (4)")
        array = crea()
        somma_array = somma(array)
        media_array = media(array)
        utente = input("Inserire l'operazione: ")
        if utente == "1":
            print(array)
        elif utente == "2":
            print(somma_array)
        elif utente == "3":
            print(media_array)
        else:
            break
menù()
