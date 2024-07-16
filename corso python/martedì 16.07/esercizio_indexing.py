#ESERCIZIO 3 = Operazioni con Francy Indexing
import numpy as np

def crea():
    matrice = np.random.randint(10, 50,16)                 #matrice 4x4 con numeri casuali che vanno da 10 a 50
    matrice = matrice.reshape(4,4)
    print(matrice)
    return matrice

def stampa_elem(matrice):
    indici = np.array([[0, 1], [1, 3], [2, 2], [3, 0]])     #selezionare e stampre gli elemnti degli indici [0, 1], [1, 3], [2, 2], [3, 0]
    elementi = matrice[indici[:, 0], indici[:, 1]]
    print(elementi)
    return elementi

def stampa_righe(matrice):
    righe_dispari = matrice[1::2, :]                        #stampare le righe dispari dell'array
    print(righe_dispari)
    return(matrice)

def cambia_inidice(matrice):
    indici = np.array([[0, 1], [1, 3], [2, 2], [3, 0]]) 
    matrice[indici[:, 0], indici[:, 1]] += 10               #modificare gli indici del primo punto aggiungendo 10 al loro valore
    print(matrice)
    return(matrice)