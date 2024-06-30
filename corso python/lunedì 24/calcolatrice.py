#create una calcolatrice semplificata che fa operazione solo su 2 numeri, 
#l'utente inserisce primo numero, secondo numero e operazione matematica 
#e il programma ci restituisce il risultato


primo_numero=int(input("Inserisci il primo numero: "))
secondo_numero=int(input("Inserisci il secondo numero: "))
print("Scegli tra le seguenti operazioni: Addizione, Sottrazione, Moltiplicazine e Divisione: ")
utente=input("Quale operazione scegli? ")

if utente == "Addizione":
    print(primo_numero+secondo_numero)
elif utente == "Sottrazione":
    print(primo_numero-secondo_numero)
elif utente == "Moltiplicazione":
    print(primo_numero*secondo_numero)
elif utente == "Divisione":
    print(primo_numero/secondo_numero)
else:
    print("Operazione non valida")