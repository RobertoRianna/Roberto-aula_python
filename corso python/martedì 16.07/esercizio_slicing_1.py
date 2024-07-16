#esercizio slicig e fancy indixing

import numpy as np

matrice2D = np.random.randint(1, 101,36)                #matrice 6x6 con numeri casuali che vanno da 1 a 100
matrice2D = matrice2D.reshape(6,6)
print(matrice2D)

sotto_matrice2D = matrice2D[1:5, 1:5]                   #sotto matrice 4x4
print(sotto_matrice2D)

print(sotto_matrice2D[::-1])                            #invertire le righe della matrice 4x4


array1D = np.diagonal(sotto_matrice2D)                      #stampa la diagonale principale della sotto matrice
print(array1D)

sotto_matrice2D[sotto_matrice2D % 3 == 0] = -1          #sostituisce gli elementi che sono multipli di 3 con -1
print(sotto_matrice2D)



