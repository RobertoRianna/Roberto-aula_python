import numpy as np

def crea_array():
    array = np.linspace(8,10,50)                                        #crea un aray di 50 numeri equidistanti da 8 a 10
    return array

def crea_random():
    random_array = np.random.random(50)                                 #50 numeri casuali compresi tra 0 a 1
    return random_array

def somma_array(array, random_array):
    array_somma = array + random_array                                  #somma dei due array elemento per elemento
    return array_somma

def somma_totale(array_somma):
    somma_array_nuovo = np.sum(array_somma)                                         #somma array nuovo
    return somma_array_nuovo

def somma_maggiore(array_somma):
    array_maggiore5 = array_somma > 5
    somma_array_maggiore5 = np.sum(array_maggiore5)                                 #somma elementi maggiore di 5 del nuovo array
    return somma_array_maggiore5


def menù():
    controllo = True
    while controllo:
        print("Menù")
        print("Crea un array (1) ")
        print("Crea un array random (2) ")
        print("Somma i due array (3) ")
        print("Somma totale array nuovo (4) ")
        print("Somma elementi maggiori di 5 (5) ")
        print("Exit (6) ")
        utente = input("Inserisci l'operazione da fare: ")
        array = crea_array()
        random_array = crea_random()
        array_somma = somma_array(array,random_array)
        somma_array_nuovo = somma_totale(array_somma)
        array_maggiore5 = somma_maggiore(array_somma)
        if utente == "1":
            print(array)
        elif utente == "2":
            print(random_array)
        elif utente == "3":
            print(array_somma)
        elif utente == "4":
            print("La somma totale dell'array nuovo è: ",somma_array_nuovo)
        elif utente == "5":
            print("La somma totale dell'array con gli elementi maggiori di 5 è: ",array_maggiore5)
        else:
            break

menù()