print("Menu")
print("Aggiungi")
print("Rimuovi")
print("Visualizza")
print("Esci")
scelta=input("Selezione un'opzione: ")

if scelta == "Aggiungi":
    elemento=input("Inserisci l'elemento da aggiungere")
    lista.append(elemento)
    print("elemento")

elemento=input("Inserisci l'elemento da rimuovere: ")
if elemento =="Rimuovi":
        lista.remove(elemento)
        print("elemento")
elemento=input("Inserisci l'elemento da visualizzare: ")
if elemento =="visualizza" :

    
        