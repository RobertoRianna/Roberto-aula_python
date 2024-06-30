#Scrivete una programma che richiede una lista di numeri all’utente e fornisce in output un istogramma basato su questi 
#numeri, usando asterischi per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questasequenza:
#***
#*******
#*********
#*****

controllo=True
lista_numeri=[]
while controllo:
    
    utente=input("Vuoi inserire un numero? (sì/no)")
    numero=int(input("Inserisci un numero: "))
    if utente == "sì":
        lista_numeri.append(numero)                 #aggiunge il numero nella lista

    elif utente == "no":
        break

    for i in lista_numeri:                  #stampa gli asterischi per quanto è il numero
        print("*"*(i))                      #esempio:numero 3 = 3 asterischi                                    