class ContoBancario:
    def __init__(self,titolare,saldo):
        self.__titolare = titolare
        self.__saldo = saldo
        
    
    def deposita(self):
        importo =int(input("Aggiungi un importo: "))
        if importo > 0:
            self.__saldo += importo
        elif importo <= 0:
            print("Importo negativo, non valido!")
    
    def preleva(self):
        importo1 = int(input("Aggiungi l'importo che vuoi prelevare: "))
        if importo1 < self.__saldo:
            self.__saldo -= importo1
        else:
            print("Importo non presente")
    
    def visualizza_saldo(self):
        print(self.__saldo)


#mi mancano i metodi getter e setter che non ho capito come si usano


conto1= ContoBancario("rob",0)
conto1.deposita()
conto1.preleva()
conto1.visualizza_saldo()


        