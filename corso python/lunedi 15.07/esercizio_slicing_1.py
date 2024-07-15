#esercizio su numpy slicing
import numpy as np

array1D = np.arange(20,40)           #crea un array da 20 a 39                  
print(array1D)

print(array1D[0:10])                #stampa i primi 10 elementi di un array

print(array1D[-5: ])                #stampa gli ultimi 5 elementi

print(array1D[5:15])                #stampa gli elementi dall'indice 5 a 15(escluso)

print(array1D[0:40:3])              #stampa gli elementi dell'array ogni 3 

array1D [5:10] = 99                 #modifica gli elementi da 5 a 10(escluso) con 99
print(array1D)


