import numpy as np

controllo = True
while controllo:
    utente= input(print("Vuoi eseguire l'operazione: (sì) "))
    if utente == "sì":
        arr = np.arange(10,50)                                                      #creo un array che va da 10 a 49
        print(arr)

        print("Tipo di dato: ",arr.dtype)                                           #stampo il tipo di dato

        arr = arr.astype('float64')                                                 #converto il tipo di dato in float
        print("Tipo di dato aggiornato: ",arr.dtype)                                #stampo il nhovo tipo di dato

        print("forma dell'array: ",arr.shape)                                       #stampo la forma dell'array
    else:
        break