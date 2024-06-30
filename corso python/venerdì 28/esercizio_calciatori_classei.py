#Create una classe calciatore che ha come attributi:
#-nome:
#-ruolo:
#- valore.
#Create un metodo getter per avere solo i valori dei calciatori e un metodo setter per settare il ruolo del calciatore.
#Create almeno 3 calciatori e poi printate in ordine di valore i calciatori.

class Calciatori:
    def __init__(self,nome,ruolo,valore):                     #specifichiamo gli argomeni della classe
        self.nome= nome 
        self.ruolo= ruolo
        self.valore= valore

    def visualizza_valore(self):                              #ci stampa il valore
        return self.valore
    
    def inserisci_ruolo(self):                                #inserisci il ruolo
        self.ruolo = input("Inserisci il ruolo: ")
    


Giovanni= Calciatori("Giovanni","difensore",[8])
Ciro= Calciatori("Ciro","attaccate",[10])
Lorenzo=Calciatori("Lorenzo","portiere",[6])

Giovanni.visualizza_valore()
Ciro.visualizza_valore()
Lorenzo.visualizza_valore()

Giovanni.inserisci_ruolo()
Ciro.inserisci_ruolo()
Lorenzo.inserisci_ruolo()



