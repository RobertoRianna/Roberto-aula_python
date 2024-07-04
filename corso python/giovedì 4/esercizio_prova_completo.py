class Posto:
    def __init__(self,numero,fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = True

    def stampa(self):
        print("Visualizza: il posto numero: ", self.__numero, "della: ",self.__fila)

    def get_numero(self):
        return self.__numero
        
    def get_fila(self):
        return self.__fila
    
    def prenota(self):
        if self.__occupato:
            print("Il posto è occupato")
        elif self.__occupato == False:
            print("Hai prenotato il posto")

    def libera(self):
        if self.__occupato:
            self.__occupato == False
            print("il posto ora è libero")
        
        elif self.__occupato == False:
            return

    




class PostoVip(Posto):
    def __init__(self, numero, fila,servizi_extra):
        super().__init__(numero, fila)
        self.__servizi_extra = servizi_extra
    
    def prenota(self):
        print("L'",self.__servizi_extra,"è consentito solo ai maggiorenni")
        return super().prenota()


class PostoStandard(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
    
    def prenotazione_online(self):
        utente = input("Vuoi prenotare online: (sì/no) ")
        if utente == "sì":
            print("Il costo ha un'aggiunta di 2 euro")
        elif utente == "no":
            print("Vi aspettiamo alla cassa")


class Teatro():
    def __init__(self):
        self.__posti = [1,2,3,4,5,6,7,8,9]
    
    def prenota_posto(self):
        utente = int(input("Inserisci il numero del posto: (da 1 a 9)"))
        if utente in self.__posti:
            print("Il posto è libero")
            self.__posti.remove(utente)
            
        else:
            print("Il posto non è presente")

    def stampa_posti_occupati(self):
        print("i posti liberi sono: ", self.__posti)







posto1 = Posto(10,"fila 5")
posto1.stampa()
posto1.prenota()
posto1.libera()

x=posto1.get_numero()
y=posto1.get_fila()
print(x)
print(y)

posto2= PostoVip(20,1,"accesso alla sala fumatori")
posto2.prenota()

posto3= PostoStandard(50,3)
posto3.prenotazione_online


teatro1= Teatro()
teatro1.prenota_posto()
teatro1.stampa_posti_occupati()

