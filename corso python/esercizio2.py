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
              numero1-1
 #??????   
#non mi fa aggiungere Else o Elif, neache break. se inserisco controllo = False non mi ferma il loop
            
        
         
         



#Punto 3

lista_numeri=[]
for numero in lista_numeri:
      
    numero=int(input("Inserisci un numero: "))
    print(numero * numero)
    lista_numeri.append(numero)



