#Create un programma che richiede all’utente Nome, anno di
#nascita e giorno della settimana (a numero) e stampa in
#maniere formattata oltre al nome, l’età e i giorni che mancano
#al prossimo weekend (sabato):
#Esempio
#’Il tuo nome è Tommaso, hai 37 anni e mancano 5 giorni al
#weekend’

nome=input("Inserisci il tuo nome: ")
anno=int(input("Inserisci il tuo anno di nascita: "))
giorno=int(input("Inserisci il giorno della settimana a numero: "))

età=anno- 2024
giorno_della_settimana=giorno - 6



print("Il tuo nome è: ",nome,  "hai", età , "anni e mancano " ,giorno_della_settimana ,"giorni al weekend")



