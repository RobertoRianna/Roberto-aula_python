stringa = "il cane nuota"
print("La stringa è: " + stringa + "")
print("Aggiungi, Rimuovi, Sostituisci")
scegli=input("Scegli una delle opzioni riportate sopra")
if(scegli=="Aggiungi"):
    parola=input("inserisci la parola da aggiungere: ")
    print(stringa +" " + parola)
elif(scegli=="Sostituisci"):
    rimuovi=input("Inserisci la prola da rimuovere: ")
    parola=input("INserici la parola da aggiungere: ")
    print(stringa.replace(rimuovi,parola))
else:
    parola=input("Inserisci la parola da rimuovere: ")
    print(stringa.replace(parola,""))
