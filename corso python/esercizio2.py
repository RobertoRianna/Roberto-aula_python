#esercizio su Cicli e Condizioni
#Punto 1

numero=int(input("Inserisci un numero: "))
if numero % 2 == 0:                         #verifica se il numero è pari
    print("Il numero è pari")    
else:
    print("Il numero è dispari")


#Punto 2: Utilizzo di while e range

controllo= True    #istruzione di controllo

while controllo:    
       numero1=int(input("Inserisci un numero intero positivo: "))
       
       for i in range(numero1,-1,-1):      #stampa dal numero inserito dall'utente a zero(compreso)
              print(i)
              numero1-1                     



#Punto 3


