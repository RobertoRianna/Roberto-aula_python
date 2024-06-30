#chiedi all'utente l'età
età=input("quanti anni hai?")

if età < "18":
    print("Mi dispiace non puoi vedere questo film!")
else:
    print("puoi stampare questo film")
    

#Inserisci in input 2 numeri e scegli quale delle 4 operazioni fare
numero_1=input("Inserisci il primo numero: ")
numero_2=input("INserisci il secondo numero: ")

print("Addizione, Sottrazione, Divisione, Moltiplicazione")
operazione=input("Quale operazione vuoi eseguire?")
if operazione == "Addizione":
    print(numero_1 + numero_2)

elif operazione == "Sottrazione":
    print(numero_1 - numero_2)

elif operazione == "Divisione":
    print(numero_1 / numero_2)

elif operazione == "Moltiplicazione":
    print(numero_1 * numero_2)
else:
    print("Operazione non valida")





    


    
