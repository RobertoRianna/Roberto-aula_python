#crea un esercizio che rappresenti quello che hai inparato nella settimana precedente.

controllo= True                                                             #imposto un controllo 

while controllo:                        
    print("Menù di cosa ho imparato: ")                                        #ho creato un menù
    print("Dizionari (Digita: 1)")
    print("File esterno (Digita: 2)")
    print("Funzioni (Digita: 3)")
    print("Classi (Digita: 4)")
    utente=input("Inserisci cosa vuoi vedere: ")                                #prendo in input la scelta dell'utente

    if utente == "1":
        utente1={"nome": "roberto","cognome":"rianna","età":23}
        print(utente1["età"])                                               #stampa età
                                                
        for element in utente1.values():                               
            print(element)                                                  #stampa tutti i valori


    elif utente == "2":
        with open("text.txt", "w") as file:                #crea il file e scrive ciao, se esiste già cancella quello che c'è e scrive ciao
            file.write("ciao ")
        
        with open("text.txt","a") as file:                 #scrive "a tutti" se già esiste  il file
            file.write("a tutti")
        
        with open("text.txt","r") as file:                  #stampa il contenuto del file
            contenuto = file.read()
            print(contenuto)


    elif utente == "3":
        

        from random import randint                      #importa la funzione e ci da un numero casuale da 1 a 50
        print(randint(1,50))


        from random import choice                       
        lista=["uno","due","tre","quattro"]             #ci da un valore random che è presente nella lista
        print(choice(lista))

    elif utente == "4":
        class Studenti:                                                 #abbiamo creato una classe
            def __init__(self,nome,cognome,voti):                       #specifichiamo gli argomeni della classe
                self.nome= nome 
                self.cognome=cognome
                self.voti=voti
            def visualizza_nome(self):                                   #funzione che ci stampa il nome
                print(self.nome)

        Giovanni= Studenti("Giovanni","Rossi",[6,7])
        Giovanni.visualizza_nome()                                      #stampa il nome di Giovanni

        print(Giovanni)                                                 #stampa lo spazio di memoria di dov'è contenuto
        print(Giovanni.voti)                                             #stampa i voti di Giovanni
        


        
        


