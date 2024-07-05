""" Le tre regole fondamentali dell'OOP sono: Polimorfismo, Incapsulamento, ereditarietà.
Il polimorfismo permette di trattare oggetti di classi diverse e lo usiamo principalmente 
quando facciamo la sovrascrittura. Possiamo definire il Polimorfismo con: cambia forma ma non il comportamento. 
L'incapsulamento nasconde i dettagli interni di una classe e utilizza 3 metodi: Attributi privati, Attributi protetti, metodi Getter e Setter.
Gli attributi privati: significa che non  può esserci accesso direttamente dall'esterno della classe e si utilizzano aggiungendo (_ _).
Attributi Protetti: dovrebbe essere usato solo all'interno della classe e delle sue sottoclassi e si usa aggiungendo (_).
Metodi Getter e Setter: Sono metodi che permettono di ottenere (get) e modificare (set) gli attributi privati di una classe.
L'Ereditarietà ci permette di riutilizzare il codice e utilizza 3 metodi: super(), Sovrascrittura dei metodi, Ereditarietà Multipla.
super(): Questa funzione è usata per richiamare la classe Padre, permettendo alla classe Figlia di estendere o modificare i metodi e gli 
attribbuti della classe Padre.
Sovrascrittura di metodi: La classe Figlia può utilizzare i metodi della classe Padre per modificare o estendere il loro comportamento
Ereditarietà Multipla: permettendo a una classe di ereditare da più classi base. Questo può essere realizzato
elencando le classi Padre tra parentesi durante la definizione della sottoclasse """

#ESEMPIO DI POLIMORFISMO

class Zoo:
    def __init__(self,nome,città):
        super.nome = nome
        super.città = città

class Elefante(Zoo):
    def __init__(self, nome, città,peso):
        super().__init__(nome, città)
        super.peso = peso