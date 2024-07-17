#ESERCIIZO 2: manipolazione e aggregazione dei dati

import pandas as pd


def crea():
    data = {
        'Prodotto': ['Palla', 'Osso', 'Crocchette', 'Guinzaglio', 'Collare'],
        'Quantità': [10, 20, 30, 15, 15],
        'Prezzo Unitario': [3.00, 2.00, 50.00, 8.00, 12.00],
        'Città': ['Napoli', 'Caserta', 'Benevento', 'Avellino', 'Salerno']
    }
    df = pd.DataFrame(data)
    return df

def aggiungi(df):
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    return df

def totale_prodotto(df):
    totale_vendite1 = df.groupby('Prodotto')['Totale Vendite'].sum()
    return totale_vendite1


def prodotto_venduto(df):
        totale_prodotto1 =df.groupby("Prodotto").agg({"Quantità": "sum"}) 
        prodotto_piu_venduto = totale_prodotto1.loc[totale_prodotto1["Quantità"].idxmax()]
        return prodotto_piu_venduto

def totale_vendite(df):
    vendite_citta = df.groupby('Città')['Totale Vendite'].sum()
    return vendite_citta


def crea_nuovo():
    data = {
        'Prodotto': ['Acqua', 'Pane', 'Banana', 'Carota', 'Sedano'],
        'Quantità': [5, 10, 15, 8, 9],
        'Prezzo Unitario': [2.50, 3.00, 2.00, 4.00, 1.50],
        'Città': ['Frosinone', 'Milano', 'Torino', 'Cagliari', 'Roma']
    }
    df1 = pd.DataFrame(data)
    df1['Totale Vendite'] = df1['Quantità'] * df1['Prezzo Unitario']

    soglia_vendite = 100
    vendite_superiori = df1[df1['Totale Vendite'] > soglia_vendite]
    return df1,vendite_superiori


def ordina(df):
    df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
    return df_ordinato


def visualizza(df):
    numero_vendite = df.groupby("Città").agg({"Totale Vendite":"sum"})
    return numero_vendite