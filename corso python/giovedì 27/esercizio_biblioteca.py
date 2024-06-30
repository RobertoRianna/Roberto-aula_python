#Create un programma per la gestione di una biblioteca, il programma può avere 2 tipi di utenti:
#utente amministratore può:
#-vedere i libri presenti e se sono in prestito o disponibili
#-eliminare o aggiungere un libro
#il libro ha:-titolo -autore -anno -stato prestito

#listaLibri = [["libro1", "titolo1", "autore1", 2024, "stato = True"], ["libro2", "titolo2", "autore2", 2023, "stato = True"]]


libro1 = "Libro1,Autore1,2001,Disponibile"
libro2 = "Libro2,Autore2,2016,Prestito"
libro3 = "Libro3,Autore3,2004,Prestito"

listaLibri = [libro1, libro2, libro3]
print(listaLibri)

def presenteLibro():
    titolo = input("Inserisci il titolo del libro: ")
    trovato = False

    for libro in listaLibri:
    
        libroSplittato = libro.split(",")
    
        if titolo == libroSplittato[0]:
            trovato = True
            print("Libro presente")
            print(libro)
            break

    if not trovato:
        print("Libro non trovato")

def aggiungiLibro():
    
    nuovoLibro = input("Inserisci le informazioni del libro nel formato 'titolo,autore,anno,stato': ")
    with open("libri.csv", "a") as file:
        file.write("\n" + nuovoLibro)
    
    with open("libri.csv", "r") as file:
        contenuto = file.read()
    print(contenuto)

def letturaLibri():
    with open("libri.csv", "r") as file:
        contenuto = file.read()
    print(contenuto) 


login = input("sei amministratore o utente? ")
nome = "admin"
password = "1234"

if login.lower() == "utente":
    pass
elif login.lower() == "amministratore":
    nome_input = input("inserire username: ")
    pass_input = input("inserisci la password: ")
    if nome_input == nome and pass_input == password:
        print("Credenziali corrette. Benvenuto!")
    
    print("Menu: ")
    print("1. Lettura Elenco Libri")       
    print("2. Aggiungi Libro")
    print("3. Elimina Libro")
    cod = int(input("Scegli un opzione: "))
    if cod == 1:
        letturaLibri()
    elif cod == 2:
        aggiungiLibro()
    