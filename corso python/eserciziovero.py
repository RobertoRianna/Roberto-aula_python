#parte 1
controllo= True 
selezione= input("Vuoi iniziare?")

inventario=["Papera", "Anello", "Bracciale"]
acquisti_cliente=[]

if selezione == "sì":

    while controllo:
        selezione2= input("Vuoi vedere i prodotti?")
        if selezione2 == "sì":
            print(inventario)
            articolo=input("Quale vuoi comprare? ")
            print(articolo)
            acquisti_cliente.append(articolo)
        elif selezione2 == "no":
            break
            
        



#parte 2

#liste dei 3 prodotti

Papera=["Papera di gomma", "5 euro", "20 pezzi"]
Anello=["Anello di oro","50 euro", "10 pezzi"]
Bracciale=["Bracciale in acciaio", "15 euro", "5 pezzi"]

#aggiunta ad una lista
inventario.append("osso")
inventario.append("barca")

#modifica ad una lista
Papera[1]= "6 euro"
Anello[2]= "20 pezzi"

#rimuove ad una lista
Bracciale.remove("5 pezzi")

#stampa lista aggiornata
print(Papera)
print(Anello)
print(Bracciale)


#parte 3


stato_corrente=[Papera[1], Anello[1], Bracciale[1]]
guadagni_totali=[Papera[1], Anello[1], Bracciale[1]] #come si sommano?

if selezione == "sì":

    while controllo:
        vendite= input("Vuoi visualizzare il rapporto vendite? ")
        if vendite == "sì":
            print(acquisti_cliente)
        stato_corrente1= input("Vuoi visualizzare lo stato corrente? ")
        if stato_corrente1 == "sì":
            print(stato_corrente)
        guadagni= input("Vuoi visualizzare i guadagni totali ?")
        if guadagni == "sì":
            print(guadagni_totali)
        break

            
           







        