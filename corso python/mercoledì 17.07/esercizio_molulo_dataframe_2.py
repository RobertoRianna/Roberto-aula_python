#ESERCIIZO 2: manipolazione e aggregazione dei dati
#diviso in moduli - vedere esercizio_dataframe_2.py

import pandas as pd                                                                     #importo la libreria pandas


def crea():                                                                             #creo un dataframe
    data = {
        'Prodotto': ['Palla', 'Osso', 'Crocchette', 'Guinzaglio', 'Collare'],
        'Quantità': [10, 20, 30, 15, 15],
        'Prezzo Unitario': [3.00, 2.00, 50.00, 8.00, 12.00],
        'Città': ['Napoli', 'Caserta', 'Benevento', 'Avellino', 'Salerno']
    }
    df = pd.DataFrame(data)
    return df

def aggiungi(df):                                                                       #aggiungo la colonna totale vendite che contiene il prodoto 
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']                       #tra quantità e prezzo unitario
    return df

def totale_prodotto(df):                                                                #totale vendite per ciascun prodotto
    totale_vendite1 = df.groupby('Prodotto')['Totale Vendite'].sum()
    return totale_vendite1

def prodotto_venduto(df):                                                               #trova il prodotto piu venduto in termini di quantità
        totale_prodotto1 =df.groupby("Prodotto").agg({"Quantità": "sum"}) 
        prodotto_piu_venduto = totale_prodotto1.loc[totale_prodotto1["Quantità"].idxmax()]
        return prodotto_piu_venduto

def totale_vendite(df):                                                                 #cerca la città con il maggior valume di vendite totali
    vendite_citta = df.groupby('Città')['Totale Vendite'].sum()
    return vendite_citta

def crea_nuovo():                                                                       #creo un nuovo dataframe
    data = {
        'Prodotto': ['Acqua', 'Pane', 'Banana', 'Carota', 'Sedano'],
        'Quantità': [5, 10, 15, 8, 9],
        'Prezzo Unitario': [2.50, 3.00, 2.00, 4.00, 1.50],
        'Città': ['Frosinone', 'Milano', 'Torino', 'Cagliari', 'Roma']
    }
    df1 = pd.DataFrame(data)                                                            #mostra le vendite solo superiori a 100
    df1['Totale Vendite'] = df1['Quantità'] * df1['Prezzo Unitario']

    soglia_vendite = 100
    vendite_superiori = df1[df1['Totale Vendite'] > soglia_vendite]
    return df1,vendite_superiori

def ordina(df):                                                                         #ordina il dataframe in ordine decrescente 
    df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)                  #basandosi sulla colonna totale vendite                 
    return df_ordinato

def visualizza(df):                                                                     #visualizza il numero di vendite per ogni città
    numero_vendite = df.groupby("Città").agg({"Totale Vendite":"sum"})
    return numero_vendite