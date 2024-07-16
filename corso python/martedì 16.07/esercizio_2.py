import numpy as np

array = np.linspace(0,1,12)             #crea un aray di 12 numeri equidistanti da 0 a 1
print(array)

array = array.reshape(3,4)              #cambia la forma in 3x4
print(array)

random_array = np.random.rand(3,4)      #matrice 3x4 di numeri causuali da 0 a 1
print(random_array)

somma_array = np.sum(array)             #somma array
print(somma_array)

somma_random_array = np.sum(random_array)       #somma array random
print(somma_random_array)
