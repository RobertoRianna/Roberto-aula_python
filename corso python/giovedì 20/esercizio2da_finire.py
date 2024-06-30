#esercizio su Cicli e Condizioni
#Punto 1
controllo= True 

while controllo:
    numero=int(input("Inserisci un numero: "))
    if numero % 2 == 0:                         #verifica se il numero è pari
        print("Il numero è pari")    
    else:
        print("Il numero è dispari")
        controllo=False 


#Punto 2: Utilizzo di while e range

controllo= True    #istruzione di controllo

while controllo:    
       numero1=int(input("Inserisci un numero intero positivo: "))
       if numero1 > 0:
            for i in range(numero1,-1,-1):      #stampa dal numero inserito dall'utente a zero(compreso)
              print(i)
            if numero1<0:                       #SE IL NUMERO è MINORE DI 0 ESCE DAL CICLO
                break
              





            
        
#Punto 3: Utilizzo di for

controllo= False     
lista_numeri=[]
if controllo== False:
    numeri=int(input("Inserisci un numero: "))      #inserisce il numero nella lista
    lista_numeri.append(numeri)                        #esegue il quadrato dee numero
    

    for numero in lista_numeri:                     #!!!non entra nel for!!!!!
        cliente=(input("Vuoi inserire un numero?  "))
        if cliente == "sì":
            numeri=int(input("Inserisci un numero: "))
            lista_numeri.append(numeri)            #Inserisce il numero nella lista
            numeri=numeri * 2                       #esegue il quadrato di un numero
            print(lista_numeri)
        else:
            controllo == True                       #esce dal ciclo
        
        
        
#Punto 4: Utilizzo di if, while e for

controllo=True 
lista_numeri_interi=[]

while controllo:
    utente=(input("Vuoi inserire un numero? "))     #Scelta dell'utente
    if utente == "sì":
        numeri1=int(input("Inserisci un numero: "))  #inserisci un numero
        lista_numeri_interi.append(numeri1)             #aggiunge i numeri nella lista

    elif utente == "no":                            
        controllo=False                                 #esce dal ciclo
    






    





