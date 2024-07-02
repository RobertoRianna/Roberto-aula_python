class Prodotto:                                                                                     #creo la classe
    def __init__(self,nome,costo_produzione,prezzo_vendita):                                        #metodo costrutture
        self.nome = nome                                                                            #attributo
        self.costo_produzione = costo_produzione                                                    #attributo
        self.prezzo_vendita = prezzo_vendita                                                        #attributo

    def calcola_profitto(self):                                                                     #funzione calcola profitto
        differenza = self.prezzo_vendita - self.costo_produzione                                    #differenza tra attributi
        print(differenza)                                                                           #stampa la differenza
        

class Elettronica:                                                                                  #creo la classe
    def __init__(self,prodotto,garanzia):                                                           #metodo costruttore
        self.prodotto = prodotto                                                                    #attributo
        self.garanzia = garanzia                                                                    #attributo
        
    


class Abbigliamento:                                                                                #creo la classe
    def __init__(self,prodotto,materiale):                                                          #metodo costruttore
        self.prodotto = prodotto                                                                    #ATTRIBUTO
        self.materiale = materiale                                                                  #attributo


prodotto1 = Prodotto("Palla", 2, 6)                                                                 #aggiungo valori alla classe "Prodotto"
prodotto1.calcola_profitto()                                                                        #richiao la funziona "calcola profitto"


class Fabbrica:                                                                                     #creo la classe
    inventario = {}                                                                                 #creo un dizionario
    def __init__(self):                                                                             #metodo costruttore
        self.inventario = {}                                                                        #attributo dizionrio
        
    
    def aggiungi_prodotto(self):                                                                    #funzione aggiunge prodotto
        prodotto1 = input("Quale prodotto vuoi aggiungere?")                                        #chiede in input quale prodotto si vuole aggiungere
        self.inventario = [prodotto1]                                                               #aggiunge il prodotto al dizionario
        






