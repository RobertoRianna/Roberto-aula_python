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








        