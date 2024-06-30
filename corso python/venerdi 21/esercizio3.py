numero=int(input("Inserisci un numero positivo: "))
controllo=True
contatore=0
while controllo:

    if numero <= 0:
        numero=int(input("Inserisci un numero positivo: "))
    elif numero >0:
        for i in range(0,numero+1):
            print(i)
            
        for a in range(0,numero+1):
            if numero%2 ==0:

                contatore=contatore+numero
                print(contatore)
            
        for b in range(0,numero+1):
            if numero%2 !=0:
                print(b)
                
        
    


    