class Prodotto:
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        differenza = self.prezzo_vendita - self.costo_produzione
        print(differenza)


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita,garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita,)
        self.garanzia = garanzia
    


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita,materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale




class Fabbrica:
    inventario = {}
    def __init__(self):
        self.inventario = {}
        
    
    def aggiungi_prodotto(self):
        prodotto1 = input("Quale prodotto vuoi aggiungere?")
        self.inventario = [prodotto1]


        
prodotto1 = Prodotto("Palla","2 euro", "6 euro")
prodotto1.calcola_profitto