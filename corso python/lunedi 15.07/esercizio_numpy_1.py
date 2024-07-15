import numpy as np

controllo = True
while controllo:
    utente= input(print("Vuoi eseguire l'operazione: (sì) "))
    if utente == "sì":
        arr = np.arange(10,50)
        print(arr)

        print("Tipo di dato: ",arr.dtype)  

        arr = arr.astype('float64')
        print("Tipo di dato aggiornato: ",arr.dtype)

        print("forma dell'array: ",arr.shape)   
    else:
        break