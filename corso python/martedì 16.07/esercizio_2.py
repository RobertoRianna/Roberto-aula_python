#esercizio lindspace, random, sum
import numpy as np

def crea_array():
    array = np.linspace(0,1,12)             #crea un aray di 12 numeri equidistanti da 0 a 1
    return array

def modifica_array(array):
    array = array.reshape(3,4)              #cambia la forma in 3x4
    return array

def array_random():
    random_array = np.random.rand(3,4)      #matrice 3x4 di numeri causuali da 0 a 1
    return random_array

def array_somma(array):
    somma_array = np.sum(array)             #somma array
    return somma_array

def random_somma(random_array):
    somma_random_array = np.sum(random_array)       #somma array random
    return somma_random_array

 

def menù():
    controllo = True
    while controllo:
        print("Menù")
        print("Crea un array (1) ")
        print("modifica array (2) ")
        print("Crea un array random (3) ")
        print("Somma primo array (4) ")
        print("somma array random (5) ")
        print("Exit (6) ")
        utente = input("Inserisci l'operazione da fare: ")
        array = crea_array()
        modificare_array = modifica_array(array)
        random_array = array_random()
        somma_array = array_somma(array)
        somma_random = random_somma(random_array)
        if utente == "1":
            print(array)
        elif utente == "2":
            print(modificare_array)
        elif utente == "3":
            print(random_array)
        elif utente == "4":
            print(somma_array)
        elif utente == "5":
            print(somma_random)
        else:
            break

menù()
    