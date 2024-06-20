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
              





            
        
#Punto 3

controllo= False     
lista_numeri=[]
if controllo== False:
    

    for numero in lista_numeri:                     #!!!non entra nel for!!!!!
        cliente=(input("Vuoi inserire un numero?  "))
        if cliente == "sì":
            numeri=int(input("Inserisci un numero: "))
            lista_numeri.append(numeri)
            numeri=numeri * 2
            print(lista_numeri)
        else:
            controllo == True
        
        
        




