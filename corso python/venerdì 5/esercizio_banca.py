#Create un gestionale bancario basato sulla programmazione a oggetti,
#la prima parte dell'esercizio riguarda solamente aggiunta,modifica ed eliminazione cliente con il suo conto bancario



class Banca:

    dizionario = {}

    def init(self):
        pass

    def aggiungi_cliente(self):
        while True: 
            nome_utente = input("Scrivi il tuo nome: ")
            codice_utente = input("Scrivi il tuo codice: ")

            if codice_utente not in Banca.dizionario:
                Banca.dizionario[codice_utente] = nome_utente
                print(f"Cliente {nome_utente} aggiunto con successo.")
                print(Banca.dizionario)
            else:
                print("Codice presente. Esiste già un conto bancario con questo codice.")

            continua = input("Vuoi aggiungere un altro cliente? (si/no) ")
            if continua.lower() != "si":
                break

    def rimuovi_cliente(self):
        codice_utente = input("Inserisci il codice del cliente di cui vuoi eliminare il conto: ")

        if codice_utente in Banca.dizionario:
            del Banca.dizionario[codice_utente]
            print("Cliente rimosso!")
            print(Banca.dizionario)
        else:
            print("Non c'è nessun cliente da rimuovere con questo codice.")




class Cliente:
    def __init__(self,saldo):
        self.__saldo = saldo

    def deposita(self):
        importo =int(input("Aggiungi un importo: "))
        if importo > 0:
            self.__saldo += importo
            print("Operazione eseguita!")
        elif importo <= 0:
            print("Importo negativo, non valido!")
    
    def preleva(self):
        importo1 = int(input("Aggiungi l'importo che vuoi prelevare: "))
        if importo1 < self.__saldo:
            self.__saldo -= importo1
            print("Operazione eseguita!")
        else:
            print("Importo non presente")
    
    def visualizza_saldo(self):
        print("Il saldo é: ",self.__saldo)
    
    def bonifico(self):

        counter = 0
        val = int(input("Inserisci la somma di denaro per effettuare il bonifico: "))

        if val < self.__saldo:
            counter += val
            self.__saldo -= counter
            print(f"Hai effettuato un bonifico di: {counter} euro e il tuo saldo attuale è: {self.__saldo} euro")
        else:
            print("Stai cercando di inviare una somma maggiore al tuo saldo. Errore!")





banca = Banca()
banca.aggiungi_cliente()
banca.rimuovi_cliente()

banca1 = Cliente(1000)
banca1.deposita()
banca1.preleva()
banca1.visualizza_saldo()
banca1.bonifico()

