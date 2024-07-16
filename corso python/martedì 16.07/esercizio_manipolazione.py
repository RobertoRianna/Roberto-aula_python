#ESERCIZIO 2: Mnipolazione di Array Multidimensionali
import numpy as np

def crea():
    matrice= np.arange(1,26)
    reshaped_arr = matrice.reshape((5,5))                                    #crea una matrice da 1 a 25, 5x5
    return reshaped_arr

def colonna(reshaped_arr):
    seconda_colonna = reshaped_arr[:,1]                                      #stampa la seconda colonna
    return seconda_colonna

def riga(reshaped_arr):
    terza_riga = reshaped_arr[2,: ]                                         #stampa la terza riga
    return terza_riga

def diagonale(reshapped_arr):
    calcolo_diagonale = np.diagonal(reshapped_arr)                      #diagonale principale della matrice
    return calcolo_diagonale



