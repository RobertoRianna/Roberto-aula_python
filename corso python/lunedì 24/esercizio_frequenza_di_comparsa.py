#Scrivete un programma che chiede una stringa all’utente e restituisce un dizionario rappresentante la "frequenza di
#comparsa" di ciascun carattere componente la stringa.
#Esempio:
#Stringa "ababcc",
#Risultato
#{"a": 2, "b": 2, "c": 2}


dizionario={}

s=input("Inserire una stringa: ")

for i in s:
    if i in dizionario:
        dizionario[i] += 1

    else:
        dizionario[i] = 1

print(dizionario)

