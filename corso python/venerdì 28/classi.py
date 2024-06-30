class Studenti:                                               #abbiamo creato una classe
    def __init__(self,nome,cognome,voti):                     #specifichiamo gli argomeni della classe
        self.nome= nome 
        self.cognome=cognome
        self.voti=voti

    def __str__(self):                                                                         #metodo che trasforma tutto in stringa
        return f"Nome: {self.nome}, Cognome: {+self.cognome}, Voti: {self.voti}"
    #print(Giovanni)                    #stampa tutta la stringa 
    
    
    def visualizza_nome(self):                              #classe che ci stampa il nome
        print(self.nome)
    
    def inserisci_nome(self):                                #inserisci il nome con input
        self.nome = input("Inserisci il nome: ")

tommaso= Studenti("tommaso","muraca",[7,8])
Giovanni= Studenti("Giovanni","Rossi",[6,7])
print(tommaso)                                                  #stampa lo spazio di memoria dov'è contenuto
print(tommaso.nome)                                             #stampa il nome
print(tommaso.voti)                                             #stampa i voti di tommaso

Giovanni.visualizza_nome()                                      #stampa il nome di Giovanni



class Persona:
    def __init__(self,nome,cognome) -> None:
        self.nome=nome
        self.cognome=cognome
    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}"
    
class Calcatore(Persona):
    def __init__(self, nome, cognome,ruolo):
        super().__init__(nome, cognome)
        self.ruolo=ruolo
    def __str__(self):
        return super().__str__() +f", Ruolo: {self.ruolo}"

antonio= Persona("Antonio","Rossi")


#---------------------------------------------------------------------------------------------------------

class Studenti:
    corpo_studentesco = 0
    ore_settimanali = 36
    def __init__(self,nome,cognome, voti):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
Studenti.corpo_studentesco+=1

def __str__(self):
    return f"Nome: {self.nome}, Cognome: {self.cognome}, Voti: {self.voti}, Ore settimanali: {self.ore_settimanali}"

def visualizza_nome(self):
    print(self.nome)

def inserisci_nome(self):
    self.nome = input("Inserisci il nome: ")


Giovanni = Studenti("Giovanni","Rossi",[7,8])

Tommaso = Studenti("Tommaso", "Muraca", [7,8])

Andrea = Studenti("Andrea", "Verdi", [10,9])

Andrea.ore_settimanali +=4

Andrea.visualizza_nome()

#-----------------------------------------------------------------------------------------------------------------
#EREDITARIETA' TRA CLASSI 
class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}"

class Calciatore(Persona):
    def __init__(self, nome, cognome, ruolo):
        super().__init__(nome, cognome)
        self.ruolo = ruolo
    
    def __str__(self):
        return super().__str__()+f", Ruolo: {self.ruolo}" 

class Allenatore(Persona):
    def __init__(self, nome, cognome, patentino):
        super().__init__(nome, cognome)
        self.patentino = patentino
    
    def __str__(self):
        return super().__str__()+ f", Patentino: {self.patentino}"
    
antonio = Persona("Antonio","Rossi")

buffon = Calciatore("Gianluigi","Buffon","Portiere")

conte = Allenatore("Antonio","Conte", "Patentino uefa")

print(antonio)
print(buffon)

print(conte)
