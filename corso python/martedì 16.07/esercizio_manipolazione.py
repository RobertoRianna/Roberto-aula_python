#ESERCIZIO 2: Mnipolazione di Array Multidimensionali
import numpy as np

def crea():
    matrice= np.arange(1,26)
    reshaped_arr = matrice.reshape((5,5))
    return reshaped_arr

def colonna(reshaped_arr):
    seconda_colonna = reshaped_arr[:,1]
    return seconda_colonna

def riga(reshaped_arr):
    terza_riga = reshaped_arr[2,: ]
    return terza_riga

def diagonale(reshapped_arr):
    calcolo_diagonale = np.diagonal(reshapped_arr)                      #diagonale principale della matrice
    return calcolo_diagonale



