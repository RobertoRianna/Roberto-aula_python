import numpy as np

array = np.linspace(8,10,50)                                        #crea un aray di 50 numeri equidistanti da 8 a 10
print("Array: ",array)

random_array = np.random.random(50)                                 #50 numeri casuali compresi tra 0 a 1
print("Array random: ",random_array)

somma_array = array + random_array                                  #somma dei due array elemento per elemento
print("la somma dei due array per ogni elemento è: ",somma_array)


somma_array_nuovo = np.sum(somma_array)                                         #somma array nuovo
print("La somma totale dell'array nuovo è: ",somma_array_nuovo)


array_maggiore5 = somma_array > 5
somma_array_maggiore5 = np.sum(array_maggiore5)                                 #somma elementi maggiore di 5 del nuovo array
print("La somma totale dell'array con gli elementi maggiori di 5 è: ",somma_array_maggiore5)


