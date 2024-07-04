class Veicolo:
    def __init__(self,marca,modello,anno):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = True
        
    
    def accendi(self):
        self.__accensione = True
        print("è accesa")
    
    def spegni (self):
        self.__accensione = False
        print("è spento")
    
    def set_marca(self,marca):
        self.__marca = marca
    def set_modello(self,modello):
        self.__modello = modello
    def set_anno(self,anno):
        self.__anno = anno
    def get_marca(self):
        return self.__marca
    def get_modello(self):
        return self.__modello
    def get_anno(self):
        return self.__anno

    def stampa_marca_nuova(self):
        print("la marca nuova è: ",self.__marca)



class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.__numero_porte = numero_porte
    
    def suona_clacson(self):
        print("L'auto suona il clacson")

class Furgone(Veicolo):
    def __init__(self, marca, modello, anno,capacità_carico):
        super().__init__(marca, modello, anno)
        self.__capacità_carico = capacità_carico
    
    def carica(self):
        print("Carica il furgone")
    def scarica(self):
        print("SCarica il furgone")



class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno,tipo):
        super().__init__(marca, modello, anno)
        self.__tipo = tipo
    
    def esegui_wheelie(self):
        if self.__tipo == "sportiva":
            print("Fai un trick")
        else:
            print("Nessun trick")

class GestioneParcoVeicoli(Veicolo):
    def __init__(self, marca, modello, anno):
        super().__init__(marca, modello, anno)
        self.__veicoli = []
    
    def aggiungi_veicoli(self,veicolo):
        self.__veicoli.append(veicolo)
        print("Veicolo aggiunto ")
    
    def rimuovi_veicolo(self):
        for veicolo in self.__veicoli:
            self.__veicoli.remove(veicolo)
            print("Veicolo rimsso")
    
    def lista_veicoli(self):
        for veicolo in self.__veicoli:
            print("La marca:", self.__marca,"del modello: ",self.__modello,"dell'anno:",self.__anno)



veicolo1= Veicolo("mercedes","GLA",2020)
veicolo1.accendi()
veicolo1.spegni()
veicolo1.set_marca("audi")
veicolo1.stampa_marca_nuova()

gestione1= GestioneParcoVeicoli("ferrari","spider",2000)


gestione1.aggiungi_veicoli(Auto("Fiat", "500", 2020, 4))
gestione1.aggiungi_veicoli(Furgone("Mercedes", "Sprinter", 2018, 1000))
gestione1.aggiungi_veicoli(Motocicletta("Yamaha", "R1", 2021, "sportiva"))
gestione1.lista_veicoli()
