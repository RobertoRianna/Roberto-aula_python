#DOVETE USARE TUTTE E 3 LE REGOLE FONDAMENTALI E DEVE RAPPRESENTARE QUALCOSA DI REALE

class Squadra:                                                                                                              #creo classe squadra
    def __init__(self,nome,città,numero_difensori):                                                                         #metodo costruttore
        self.__nome = nome                                                                                                  #attributo di stanza
        self.__città = città                                                                                                #attributo di istanza
        self.numero_difensori = numero_difensori                                                                            #attributo di istanza

    def modulo(self):                                                                                                       #metodo (modulo)
        print("La squadra: ",self.__nome,"è adatta a giocare con più moduli quando ha almeno: ",self.numero_difensori,"difensori")


    def set_città(self,città):                                                                                              #metodo che setta la città
        self.__città = città
    
    def get_città(self):                                                                                                    #metodo get per la città
        return self.__città



class Tre_difensori(Squadra):                                                                                               #creo la classe
    def __init__(self, nome, città,numero_difensori):                                                                       #metodo costruttore
        super().__init__(nome, città,numero_difensori)                                                                      #richiamo la classe Padre con super()

    def modulo(self):                                                                                                       #metodo (modulo)
        if self.numero_difensori >= 6 and self.numero_difensori <= 8:                                                       #uso un if per capire qunti difensori ci sono
            print("Oggi può giocare con il modulo 3-4-3 visto che ha a disposizione: ",self.numero_difensori,"difensori")   #stampo il modulo 
        else:
            pass



class Quattro_difensori(Squadra):                                                                                           #creo la classe
    def __init__(self, nome, città,numero_difensori):                                                                       #metodo costruttore
        super().__init__(nome, città,numero_difensori)                                                                      #richiamo la classe padre con super()

    def modulo(self):                                                                                                       #metodo (modulo)
        if self.numero_difensori > 8 and self.numero_difensori <= 10:                                                       #uso if per capire quanti difensori ci sono
            print("Oggi può giocare con il modulo 4-4-2 visto che ha a disposizione: ",self.numero_difensori,"difensori")   #stampo il modulo
        else:
            pass 

class Cinque_difensori(Squadra):                                                                                            #creo la classe
    def __init__(self, nome, città,numero_difensori):                                                                       #metodo costruttore
        super().__init__(nome, città,numero_difensori)                                                                      #richiao la classe padre con super()

    def modulo(self):                                                                                                       #creo la classe
        if self.numero_difensori > 10:                                                                                      #uso if per capire quanti difensori abbiamo
            print("Oggi può giocare con il modulo 5-4-1 visto che ha a disposizione: ",self.numero_difensori,"difensori")   #stampo il moudlo
        else:
            pass 
        

class GestisciFormazione(Tre_difensori,Quattro_difensori,Cinque_difensori):                                                 #creo la classe
   def organizza_formazione(self,numero_difensori):                                                                         #metodo costruttore
       print(numero_difensori.modulo())                                                                                     #stampo il modulo per tutte le formazioni



#PROVE 

team1 = Squadra("Blu","Napoli",6)
team1.modulo()
team1.set_città("Afragola")

team2= Tre_difensori("blu","Napoli",7)
team2.modulo()

team3 = Quattro_difensori("blu","Napoli",9)
team3.modulo()

team4 = Cinque_difensori("blu","Napoli",12)
team4.modulo()

team5 = GestisciFormazione("blu","Napoli",15)
team5.organizza_formazione(team1)
team5.organizza_formazione(team2)
team5.organizza_formazione(team3)
team5.organizza_formazione(team4)
