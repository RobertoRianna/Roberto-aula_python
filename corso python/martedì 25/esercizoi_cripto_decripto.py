#Scrivete un programma che utilizza il cifrario di Cesare per criptare una parola o decriptarla.
#Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di una certa quantità di posti nell'alfabeto.
#Per utilizzarlo, si sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata: 
#ad esempio, se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via. Per decifrare un messaggio cifrato
#con il cifrario di Cesare bisogna  conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero di posti corrispondente alla chiave.


alfabeto = ["a","b","c","d","e","f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v" , "z"]

scelta = input("Scegli l'operazione da effettuare: cripta (c) o decripta (d)")
chiave = int(input("Inserisci la chiave numerica: "))
stringa = input("Inserisci la stringa: ")

if scelta.lower() == "c":
    stringa_criptata = ""
    for carattere in stringa:
        if carattere in alfabeto:
            indice = alfabeto.index(carattere.lower())
            nuovo_indice = (indice + chiave) % 21 # calcoliamo il nuovo indice a cui corrisponde la lettera cifrata
            #lista_da_stampare = list(stringa_criptata).append(alfabeto[nuovo_indice])
            stringa_criptata += alfabeto[nuovo_indice]
        else:
            stringa_criptata+=carattere
            print(stringa_criptata)

elif scelta.lower() == "d":
    stringa_criptata = ""
    for carattere in stringa:
        if carattere in alfabeto:
            indice = alfabeto.index(carattere.lower())
            nuovo_indice = (indice - chiave) % 21 # calcoliamo il nuovo indice a cui corrisponde la lettera cifrata
            #lista_da_stampare = list(stringa_criptata).append(alfabeto[nuovo_indice])
            stringa_criptata += alfabeto[nuovo_indice]
        else:
            stringa_criptata+=carattere
            print(stringa_criptata)
else:
    print("scelta non valida")