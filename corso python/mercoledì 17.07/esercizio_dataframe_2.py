import esercizio_molulo_dataframe_2 as Esercizio2                                                    #importo il modulo

def menù():                                                                                          #cro un menù
    controllo = True                                                                                 #imposto un controllo a True
    while controllo:                                                                                 #inizio ciclo
        print("Menù")
        print("Crea e carica i dati su un DataFrame (1) ")
        print("Aggiungi una colonna Totale Vendite (2) ")
        print("Totale vendite per ciascun prodotto (3) ")                                               #stampa tutto il menù
        print("Trovare il prodotto più venduto in termini di Quantità (4) ")
        print("Identificare le città con maggior volume di vendite totali (5) ")
        print("Crea un nuovo DataFrame e stampa le vendite superiori a 100  (6)")
        print("Ordinare il DataFrame per Totale Vendite in ordine decrescente (7)")
        print("Visualizza il numero di vendite per ogni città (8)")
        print("Exit (9) ")
        utente = input("Inserisci l'operazione da fare: ")                                          #prende in input l'azione
        df = Esercizio2.crea()                                                                      
        aggiungi_tot = Esercizio2.aggiungi(df)
        totale_vendite1 = Esercizio2.totale_prodotto(df)
        prodotto_piu_venduto = Esercizio2.prodotto_venduto(df)                                      #richiama tute le funzioni
        vendite_citta = Esercizio2.totale_vendite(df)
        df1 = Esercizio2.crea_nuovo()
        df_ordinato = Esercizio2.ordina(df)
        numero_vendite = Esercizio2.visualizza(df)
        

        if utente == "1":
            print(df)
        elif utente == "2":
            print(aggiungi_tot)                                                                         #scelte dell'utente
        elif utente == "3":
            print(totale_vendite1)
        elif utente == "4":
            print(prodotto_piu_venduto)
        elif utente == "5":
            print(vendite_citta)
        elif utente == "6":
            print(df1)
        elif utente == "7":
            print(df_ordinato)
        elif utente == "8":
            print(numero_vendite)
        else:
            break

menù()                                                                                              #richiama la funzione menù
        