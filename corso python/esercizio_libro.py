class Libro:
    def __init__(self, titolo, autore, pagine):
        self.__titolo = titolo
        self.__autore = autore
        self.__pagine = pagine

    def __str__(self):
        return f"Il libro: {self.__titolo}, E' stato scritto da: {self.__autore}, e ha: {self.__pagine}"

titolo1= Libro ("Python","Roberto","100")
print(titolo1)

        