#ciclo: while
controllo = True
somma=0
while controllo:

    numero=int(input("Inserisci un numero intero: "))  
    if numero == 0:
        somma=somma + numero                            #somma dei numeri eseguiti
        print(somma)
        break



#ciclo:for


parola=input("Inserisci una parola: ")

for i in parola:                                                            #stampa ogni lettera di una parola
    print(parola)
    

#ciclo: range


        
    numero1=int(input("Inserisci il numero fino a dove vuoi contare: "))               
    
    for i in range (0,numero1+1,2):                                                 
        print(i)


        

