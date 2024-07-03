class MembroSquadra:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età 
    
    def descrivi (self):                                                                  
        print("Il nome del membro della squadra è:",self.nome," l'età: ", self.età,"anni")



class Giocatore(MembroSquadra):
    def __init__(self, nome, età,ruolo,numero_maglia):
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def gioca_partita(self):
        print("Il giocatore nell'ultima partita ha giocato per 10 minuti")
    
class Allenatore(MembroSquadra):
    def __init__(self, nome, età,anni_di_esprienza):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esprienza

    def dirige_allenamento(self):
        print("L'allenatore divide l'allenamento del venerdì in 2 fasi: 1 ora di tattica e 1 ora di palestra")

class Assistente(MembroSquadra):
    def __init__(self, nome, età,specializzazione):
        super().__init__(nome, età)
        self.specializzazione = specializzazione
    
    def supporta_team(self):
        print("Il ",self.specializzazione, "lavora con la squadra durante tutti gli allenamenti")


membro1 = MembroSquadra("Paolo", 22)
membro1.descrivi()

giocatore1 = Giocatore("Giuseppe", 22, "Att",10)
giocatore1.gioca_partita()

allenatore1 = Allenatore("Roberto",24,1)
allenatore1.dirige_allenamento()

assistente1 = Assistente("Peppe",40,"fisioterapista")
assistente1.supporta_team()