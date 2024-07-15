import numpy as np

arr = np.array([1,2,3,4,5])                            #creazione di un array
arr2d = np.array([[1,2,3],[4,5,6]])                    #creazione array bidimensionale

arr = np.arange(10)                                     #crea una sequenza di numeri in un array
print(arr)

arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))                       #cambia la forma di un array sena modificare i dati
print(reshaped_arr)


print("forma dell'array: ",arr.shape)                             #stampa il numero di elementi per ciascun array
print("Dimensione dell'array: ",arr.ndim)                         #dimensione dell'array
print("Tipo di dati: ",arr.dtype)                                   #stampa il tipo di dato
print("Numero elementi: ",arr.size)                                 #stampa il numero degli elemnti
print("Somma degli elementi: ",arr.sum())                           #stampa la somma degli elementi
print("Media degli elementi: ", arr.mean())                         #stampa la media degli elmenti
print("Valore massimo: ",arr.max())                                 #stampa il valore massimo
print("Indice del valore massimo: ", arr.argmax())                  #stamoa lìindice massimo

