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
inventario={"Papera", "Anello", "Bracciale"}

inventario1={
    "nome": "Papera",
    "prezzo": "18 euro",
    "quantità": "2 pezzi"
}

inventrio_2={
    "nome": "Anello",
    "prezzo": "20 euro",
    "quantità": "4 pezzi"
}

inventrio_3={
    "nome": "Bracciale",
    "prezzo": "8 euro",
    "quantità": "20 pezzi"
}

inventario[4]="osso"
inventario[5]="barca"






        