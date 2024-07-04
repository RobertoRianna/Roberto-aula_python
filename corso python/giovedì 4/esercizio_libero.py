#DOVETE USARE TUTTE E 3 LE REGOLE FONDAMENTALI E DEVE RAPPRESENTARE QUALCOSA DI REALE

class Squadra:
    def __init__(self,nome,città,numero_difensori):
        self.__nome = nome
        self.__città = città
        self.numero_difensori = numero_difensori 

    def modulo(self):
        print("La squadra: ",self.__nome,"è andatta a giocare con più moduli quando ha: ",self.numero_difensori,"difensori")


    def set_città(self,città):
        self.__città = città
    
    def get_città(self):
        return self.__città



class Tre_difensori(Squadra):
    def __init__(self, nome, città,numero_difensori):
        super().__init__(nome, città,numero_difensori)

    def modulo(self,numero_difensori):
        
        if self.numero_difensori >= 6 and self.numero_difensori <= 8:
            print("Oggi può giocare con il modulo 3-4-3 visto che ha a disposizione: ",self.numero_difensori,"difensori")
        else:
            pass


class Quattro_difensori(Squadra):
    def __init__(self, nome, città,numero_difensori):
        super().__init__(nome, città,numero_difensori)

    def modulo(self,numero_difensori):
        
        if self.numero_difensori > 8 and self.numero_difensori <= 10:
            print("Oggi può giocare con il modulo 4-4-2 visto che ha a disposizione: ",self.numero_difensori,"difensori")
        else:
            pass 

class Cinque_difensori(Squadra):
    def __init__(self, nome, città,numero_difensori):
        super().__init__(nome, città,numero_difensori)

    def modulo(self,numero_difensori):
        
        if self.numero_difensori > 10:
            print("Oggi può giocare con il modulo 5-4-1 visto che ha a disposizione: ",self.numero_difensori,"difensori")
        else:
            pass 
        

team1 = Squadra("Blu","napoli",6)
team1.modulo()
team1.set_città("lazio")

team2= Tre_difensori("rosso","milano",7)
team2.modulo(7)

team3 = Quattro_difensori("bianco","torino",9)
team3.modulo(9)

team4 = Cinque_difensori("giallo","frosinone",12)
team4.modulo(12)

