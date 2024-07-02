class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f" IL titolo del libro è: {self.titolo}, l'autore è: {self.autore}, il suo codice ISBN è: {self.isbn}")
    

libro1 = Libro("La Lampada", "Antonio", 5050)
libro1.descrizione()


class Libreria:
    catalogo = []
    def __init__(self,libro):
        self.libro = libro
        self.catalogo = []

    def aggiungi_libro(self) :
        catalogo = [Libro]
        while True:
            
            isbn = input("Inserire il codice ISBN: ")
            catalogo.append(isbn)

            scelta = input("Vuoi ggiungere un libro? (sì)")
            if scelta != "sì":
                break
            return catalogo
    
    def rimuovi_libro(self,isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print("Il libro è stato rimosso!")
            else:
                print("Il libro non è presente!")
        
    def cerca_per_titolo(self,titolo):
        trovato = False
        for libro in self.catalogo:
            if titolo == libro:
                print(libro)
                trovato = True
            
            if trovato == False:
                print("Libro non trovato")
    
    def mostra_catalogo(self):
        num = 1
        for libro in self.catalogo:
            print(f"{num}, {libro}")
            x +=1
        
   
libro2 = Libreria("La Lampada")
libro2.aggiungi_libro()
libro2.rimuovi_libro()
libro2.cerca_per_titolo()

libro2.mostra_catalogo()





        



