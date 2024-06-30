#esercizio completo


#punto1

numero=int(input("Inserisci un numero positivo: "))
controllo=True
contatore=0  
contatore_disp=0 
while controllo:
  
  
    if numero <=0:
        print("Inserisci un numero positivo: ")
    
    elif numero >0:
        scelta=input("Vuoi inserire un altro numero (sì/no)?")
        if scelta=="sì":
            numero1=int(input("Inserisci un numero positivo: "))
        else:
            break
                                                                            #parte 2
    utente=int(input("Inserisci il numero fino a dove si deve contare: "))

    for i in range(0,utente+1):
        if utente%2==0:
            contatore=contatore+utente
            print(contatore)
        elif utente%2!=0:                                                     #parte 3
            contatore_disp=contatore_disp+utente                                
            print(contatore_disp)

                                                                                #parte 4
    numero_primo=int("Inserire un numero: ")
    
                                                     ###non so trovare il numero primo!!!!!!!!                       

            


            

