
#parte 1.base

controllo= True
while controllo:
    numero=input("Vuoi inserire un numero? (sì/no)")
    if numero== "sì":
        numero1=int(input("Inserisci un numero: "))
        if numero1 % 2 == 0:                                #controllo numero pari
            print("Il numero è pari")
        else:
            print("Il numero è dispari")

    elif numero == "no":
        stringa=input("Inserisci una stringa: ")
        if(len(stringa)%2 == 0):                            #conteggio lunghezza stringa se pari 
            print("La lunghezza della stringa è pari")
        else:
            print("La lunghezza della stringa è dispari")

#manca la chiusura del ciclo

#parte 2

controllo= True
while controllo:
    numero=input("Vuoi una lista dei numeri primi? (sì/no)")
    numero1=int(input("Inserisci il primo numero: "))
    numero2=int(input("Inserisci il secondo numero: "))

    if numero== "sì":
        
        
        for i in range (numero1,numero2+1):         
            if i%2 !=0:                                 #controllo numero primo
                print(i)
    elif numero== "no":
        for i in range(numero1, numero2+1): 
            if i%2 ==0:                                 #controlllo numero non primo

                print(i)
    else:
        break




