class Animale:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età

    def nome_età(self):
            print(f" IL nome è {self.nome}, l'età è: {self.età}")

    def fai_suono(self):
        print("Il suono:")

    

class Leone(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
        
    
    def caccia(self):
        print("Il leone caccia 2 volte al giorno")
    
    def fai_suono(self):
        print("ruggito")
   


class Scimmia(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
        
    
    def mangia(self):
        print("La scimmia mangia 10 banane al giorno")
    
    def fai_suono(self):
        print("gracidare")


class Giraffa(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
        
    
    def altezza(self):
        print("La giraffa è alta 2 metri")
    
    def fai_suono(self):
        print("landito")


animale_1 = Animale("Rio",1)

animale_2 = Leone ("Leone", 3)
animale_2.fai_suono()
animale_2.caccia()

animale_3 = Scimmia("Scimmia",8)
animale_3.fai_suono()
animale_3.mangia()

animale_4 = Giraffa("Giraffa",4)
animale_4.fai_suono()
animale_4.altezza()




