class MetodoPagamento:
    def __init__(self,importo):
        self.importo = importo 
    
    def effettua_pagamento(self):
        print("Ho effettuato il pagamento di: ", self.importo,"euro")
    
class CartaDiCredito(MetodoPagamento):
    def __init__(self, importo):
        super().__init__(importo)
    
    def effettua_pagamento(self,importo):
        print("Ho effettuato il pagamento con carta di credito dal valore: ",importo,"euro")

class PayPal(MetodoPagamento):
    def __init__(self, importo):
        super().__init__(importo)
    
    def effettua_pagamento(self,importo):
        print("Ho pagato con PayPAl un importo di ",importo,"euro")



class BonificoBancario(MetodoPagamento):
    def __init__(self, importo):
        super().__init__(importo)

    def effettua_pagamento(self,importo):
        print("Ho effettuato un pagameno con bonifico bancario ell'importo:", importo,"euro")


class GestorePagamenti(CartaDiCredito,BonificoBancario,PayPal):
    
    def metodo_pagamento (self,importo):
        print(importo.effettua_pagamento())


         


ciao = MetodoPagamento(100)
ciao.effettua_pagamento()


ciao1 = CartaDiCredito(50)
ciao1.effettua_pagamento(10)
        
ciao2 = PayPal(2)
ciao2.effettua_pagamento(300)

ciao3 = BonificoBancario(2)
ciao3.effettua_pagamento(500)

ciao4 = GestorePagamenti(1)
ciao4.metodo_pagamento(ciao1)
ciao4.metodo_pagamento(ciao2)
ciao4.metodo_pagamento(ciao3)