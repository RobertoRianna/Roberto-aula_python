class Libro:                                                                #dichiaro la classe: Libro
    def __init__(self, titolo, autore, pagine):                             #metodo costruttore
        self.__titolo = titolo                                              #attributo di instanza
        self.__autore = autore                                              #attributo di instanza
        self.__pagine = pagine                                              #attributo di instanza

    def __str__(self):                                                                                          #metodo stringa
        return f"Il libro: {self.__titolo}, E' stato scritto da: {self.__autore}, e ha: {self.__pagine} pagine"

titolo1= Libro ("Python","Roberto","100")                                   #crea un oggetto di Libro
print(titolo1)                                                              #stampa

        