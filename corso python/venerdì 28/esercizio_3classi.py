#Create tre classi:
#- classe madre mezzo;
#- Classe figlio moto;
#- Classe figlio auto.

class Madre:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}"

class Figlio_moto(Madre):
    def __init__(self, nome, cognome,modello_moto):
       super().__init__(nome, cognome)
       self.modello_moto=modello_moto
    def __str__(self):
        return super().__str__() +f", Modello_moto: {self.modello_moto}"

class Figlio_auto(Madre):
    def __init__(self, nome, cognome,modello_auto):
        super().__init__(nome, cognome)
        self.modello_auto= modello_auto
    def __str__(self):
        return super().__str__() +f", Modello_auto: {self.modello_auto}"
    
   
   





   