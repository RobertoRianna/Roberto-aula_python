class Ristorante:                                                                               #creo classe                                                        
    menu = {}                                                                                   #dizionario
    aperuta = False                                                                             #controllo booleano
    def __init__(self,nome,tipo_cucina):                                                        #metodo costruttore
        self.nome = nome                                                                        #attributo
        self.tipo_cucina = tipo_cucina                                                          #attributo
    
    def stato_apertura(self):                                                                   #funzione stato di apertura
        if self.aperuta:
            print("Aperto")
        else:
            print("chiuso")
    
    def apri_ristorante(self):                                                                  #funzione apri ristorante
        self.aperuta = True
        print("Benvenuto!")
    
    def chiudi_ristorante(self):                                                                #funzione chiudi ristorante
        self.aperuta = False
        print("Il ristorante è chiuso")
    
    def aggiungi_menu(self):                                                                    #funzione aggiungi menù
        cibo = input("Quale piatto vuoi aggiungere?")
        prezzo = input("Qual'è il prezzo? ")
        self.menu[cibo] = prezzo
    
    def togli_menu(self):                                                                       #funzione rimuovi dal menù
        cibo = input("Quale cibo vuoi eliminare?")
        self.menu.pop(cibo)
        print("Cibo eliminato")

    def descrivi_ristorante(self):                                                                  #funzione descrivi ristorante
        print("Il nome del ristorante è:",self.nome,"e il tipo di cucina è: ", self.tipo_cucina)
    
    def stampa_menu(self):                                                                         #funzione stampa menu
        for i in self.menu:
            print(i,"Prezzo:",self.menu[i])


locale = Ristorante("Biga","Pizzeria")
locale.descrivi_ristorante()

locale.stato_apertura()
locale.apri_ristorante()
locale.chiudi_ristorante()
locale.aggiungi_menu()
locale.togli_menu()
locale.stampa_menu()
