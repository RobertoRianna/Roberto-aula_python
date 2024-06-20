#parte 1
controllo= True

while controllo:
    numero=int(input("Inserisci un numero:  "))
    
    if selezione == "sì":
   
        for i in range(numero, 0, -1):
            print(i)
    else:
        print("Il numero è negativo")
        selezione=input("Vuoi ripetere?")
        if selezione == "sì":
            controllo:False 



#parte 2 (non ho avuto tempo per iniziarlo)


