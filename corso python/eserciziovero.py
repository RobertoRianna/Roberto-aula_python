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

        