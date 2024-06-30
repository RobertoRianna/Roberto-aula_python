#Scrivete un programma che utilizza una funzione che accetta come parametro una stringa passata dall’utente e restituisce in
#risposta se è palindroma o no.
#Esempio:
#‘I topi non avevano nipoti’ è palindroma
#‘Ai rimpianti rimediamo Maria’ è palindroma
#‘Ciao’ non è palindroma



def palindromo(stringa):
    contr=True
    print(stringa)
    for i in range(0,len(stringa)//2+1):
        if stringa[i]!=stringa[len(stringa)-1-i]: contr=False
        #print ("qui")
        print("Palindromo" if contr else "Non palindromo")



stringa=input("Inserisci una stringa: ").lower()
punteggiatura="!,.;-"
for let in punteggiatura:
    stringa2=stringa.replace(let,"")
palindromo(stringa2)


