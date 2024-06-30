#Create un classe libro che ha al suo interno:
#-titolo;
#- autore;
#- prezzo;
#- codice isbn viene generato automaticamente in maniera randomica ogni volta che inserito un libro;
#- stato_prestito;
#Metodo
#create poi 2 metodi:
#-Metodo sconto: per applicare lo sconto della percentuale passata al prezzo;
#-Metodo prestito: per cambiare lo stato del prestito, quindi se è libero diventa prestato, se è prestato diventa libero

from random import randint, choice
class Libro:
    alfabeto = "abcdefghilmnopqrstuvz"
    def __init__(self, titolo, autore, prezzo):
        self.__titolo = titolo
        self.__autore = autore
        self.__prezzo = prezzo
        self.__stato_prestito = "libero"
        self.__isb = choice(Libro.alfabeto).upper()+choice(Libro.alfabeto).upper()+str(randint(0,9))+str(randint(0,9))
    
    def __str__(self):
        return f"Titolo: {self.__titolo}, Autore: {self.__autore}, Prezzo: {self.__prezzo}, Stato prestito: {self.__stato_prestito}, ISBN: {self.__isb}"
    
    def sconto(self, sconto):
        if sconto < 1 or sconto >99:
            print("Sconto non valido")
        else:
            self.__prezzo = self.__prezzo -(self.__prezzo* sconto)/100
    
    def cambia_stato_prestito(self):
        if self.__stato_prestito == "libero":
            self.__stato_prestito = "prestato"
        else:
            self.__stato_prestito = "libero"


python = Libro("Corso Python", "Tommaso", 10)
python.sconto(10)
python.cambia_stato_prestito()
print(python)

python.cambia_stato_prestito()
print(python)