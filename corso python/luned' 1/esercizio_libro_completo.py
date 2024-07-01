class Libro:                                                                #dichiaro la classe: Libro
    def __init__(self, titolo, autore, pagine):                             #metodo costruttore
        self.__titolo = titolo                                              #attributo di instanza
        self.__autore = autore                                              #attributo di instanza
        self.__pagine = pagine                                              #attributo di instanza

    def __str__(self):                                                                                          #metodo stringa
        return f"Il libro: {self.__titolo}, E' stato scritto da: {self.__autore}, e ha: {self.__pagine} pagine"

titolo1= Libro ("Python","Roberto","100")                                   #crea un oggetto di Libro
print(titolo1)                                                              #stampa

class Biblioteca:
    def crea_Libro():
        libri = []
        while True:
            titolo = input("inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            pagine = input("Inseriscni le pagine: ")
            libri.append(Libro(titolo,autore,pagine))
            a = input("Vuoi aggiungere un nuovo libro: (sì)")
            if a != "sì":
                break
        return libri

libr= Biblioteca.crea_Libro()
    
      


            


        