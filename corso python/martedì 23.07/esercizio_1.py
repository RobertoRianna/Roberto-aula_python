# Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:
# - calcolo della media;
# - calcolo della deviazione standard;
# - trasformarlo in un array 5x10

import numpy as np                                                      #importo la ibreria numpy

array = np.random.randint(1, 1001, size=50)                             #creo un array unidmensionale con 50 valori che vanno da 1 a 1000

media = np.mean(array)                                                  #calcolo la media  
deviazione_standard = np.std(array)                                     #calcolo la deviazione standard
mofidica_array = array.reshape(5, 10)                                   #traformo in un array 5x10


#stampe
print(array)
print(media)
print(deviazione_standard)
print(mofidica_array)