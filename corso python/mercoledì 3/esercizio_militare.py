class UnitaMilitare:
    def __init__(self,nome,numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(self.nome, "composta da ", self.numero_soldati, "si dirige verso Napoli")
    
    def attacca(self):
        print(self.nome,"composta da ", self.numero_soldati,"attacca Napoli")

    def ritira(self):
        print(self.nome, "composta da ", self.numero_soldati, "si ritira")

class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        

    def costrisci_trincea(self):
        contatore_difese = 0
        controllo = True
        while controllo:
            utente=input("Vuoi costrire una difesa temporanea? (sì/no) ")
            if utente == "sì":
                contatore_difese +=1
        
            elif utente == "no":
                break
        print("le difese temporanee create sono: ", contatore_difese)


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def esplora_territorio(self):
        contatore_esplora = 0
        controllo = True
        while controllo:
            utente1= input("Quale area vuoi esplorare? (terra/acqua)")
            if utente1 == "terra":
                print("Esploriamo l'area via TERRA per raccogliere informazioni sul nemico!")
                contatore_esplora +=1
            elif utente1 == "acqua":
                print("Esploriamo l'area via MARE per raccogliere informazioni sul nemico!")
                contatore_esplora +=1
            else:
                print("Comando sbagliato")
                break
        print("Hai esplorato il territtorio: ", contatore_esplora,"volte")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def rifornisci_unità(self):
        contatore_rifornisci = 0
        controllo = True
        while controllo:
            utente2= input("Vuoi gestire il rifornimento o la manutenzione? ")
            if utente2 == "rifornimento":
                print("Occupatevi del rifornimento")
                contatore_rifornisci +=1
            elif utente2 == "manutenzione":
                print("Occupatevi della manutenzione")
                contatore_rifornisci +=1
            else:
                print("Comando sbagliato")
                break
        print("Hai rifornito: ", contatore_rifornisci,"unità")



class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def conduci_ricognizione(self):
        contatore_ricognizione = 0
        controllo = True
        while controllo:
            print("Mattina (1), Pomeriggio (2), Sera (3)")
            utente3= input("Quale turno vuoi fare? (1,2,3)")
            if utente3 == "1":
                print("Sorveglianza di mattina")
                contatore_ricognizione +=1
            elif utente3 == "2":
                print("Sorveglianza di pomeriggio")
                contatore_ricognizione +=1
            elif utente3 == "3":
                print("Sorveglianza di sera")
                contatore_ricognizione +=1
            else:
                ("Comando sbagliato")
                break
        print("Hai eseguito: ", contatore_ricognizione, "ricognizioni")



class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    
    def calibra_artiglieria(self):
        contatore_artiglieria = 0
        controllo = True
        while controllo:
            utente4 = input("Quale arma vuoi calibrare: (fucile/arco)")
            if utente4 == "fucile":
                print("Calibrare il fucile!")
                contatore_artiglieria +=1
            elif utente4 == "arco":
                print("Calibrare l'arco!")
                contatore_artiglieria +=1
            else:
                print("Arma non presente")
                break
        print("Hai calibrato: ", contatore_artiglieria, "volte")
        

class ControlloMilitare(Fanteria,Cavalleria,SupportoLogistico,Ricognizione,Artiglieria):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.unità_registrate = {}

    def registra_unità(self,artiglieria):
        x = artiglieria.contatore_artiglieria
        
        



        
    
        







militare = UnitaMilitare("Brigata",10)
militare.muovi()
militare.attacca()
militare.ritira()

militare1 = Fanteria("Pippo",20)
militare1.costrisci_trincea()

militare2 = Cavalleria("Brbari",12)
militare2.esplora_territorio()

militare3 = SupportoLogistico("Cavaliere",5)
militare3.rifornisci_unità()


militare4= Ricognizione("Moschettiere", 8)
militare4.conduci_ricognizione()

militare5= Artiglieria("Arcieri", 20)
militare5.calibra_artiglieria()




