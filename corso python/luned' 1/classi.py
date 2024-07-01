#CLASSI
class Automobile:                                               #dichiaro la classe
    numero_di_ruote=4                                           #attributo di classe
    def __init__(self,marca,modello) :                          #metodo costruttore
        self.marca = marca                                        #sttributo di instanza
        self.modello = modello                                  #attributo di instanza

    def stampa_info(self):                                      #metodo di instanza
        print("L'automobile è una",self.marca, self.modello)

auto1=Automobile("Fiat","500")                                  #crea un oggetto di automobile
auto2= Automobile("BMW","X3")                                   #crea un altro oggetto d iAutomobile
auto1.stampa_info()                                             #stampa "L?automobile è una fiat 500"   
auto2.stampa_info()                                             #stampa "L'automobile è una BMW X3"
