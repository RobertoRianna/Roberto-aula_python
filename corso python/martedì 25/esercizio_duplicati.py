#Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, quanti sono, quali sono e quanto sono lunghi i duplicati.
#Esempio:
#‘La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito.’
#outpout
#"La" appare 2 volte, lunghezza 2.
#................................................................................................................................
#stringa =input("Inserisci una stringa: ")
stringa="La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito."


punteggiatura = [" ", ".", ",", ";", ":"]
for p in punteggiatura:
        stringa = stringa.lower().replace(p,"")

list=stringa.split(" ")

parole_incontrate={ }

for parola in list:
    parole_incontrate[parola] - list.count(parola)
lista_ripetizioni=list(parole_incontrate.values())
if max(lista_ripetizioni)>1:
      print(parole_incontrate)
else:
      print("Non ci sono ripetizioni")


     #   print(f"Il numero di volte che '{parola}' si ripete è: {list.count(parola)} e la sua lunghezza è {len(parola)}")

