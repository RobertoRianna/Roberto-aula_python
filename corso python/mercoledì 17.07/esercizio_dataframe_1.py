#ESERCIZIO 1: Analisi Esplorativa dei Dati
#Obbiettivo: Finalizzare con le operazioni di base per l'esplorazione dei dati usando pandas.
#Dataset: Utilizzare un dataset di esempio, che include le seguenti informazioni su un gruppo 
          # di persone: nome,età,città e salario

import pandas as pd
import numpy as np

def data_frame():
    nomi = ["Roberto","Antonio","Amalia","Valentina","Daniele","Danilo","Davide","Alessio","Mirko","Andrea","Lorenzo"]
    città =  ["Napoli","Torino","Benevento","Caserta","Palermo","Catania","Cagliari","Catanzaro","Frosinone","Udine","Milano"]
    data = {"Nome":np.random.choice(nomi,21),
            "Città":np.random.choice(città,21),
            "Età":np.random.randint(10,70,21),
            "Salario":np.random.randint(5000,50000,21)}
    df = pd.DataFrame(data)
    return df

def prime_ultime_righe(df):
    prime = df.head()
    ultime = df.tail()
    return prime,ultime

def tipo_dati(df):
    tipo = df.dtypes
    return tipo


def media(df):
    print("La media dell'età:")
    print(df["Età"].mean())
    print("La media del Salario:")
    print(df["Salario"].mean())

def mediana(df):
    print("La mediana dell'età:")
    print(df["Età"].median())
    print("La mediana del Salario:")
    print(df["Salario"].median())

def deviazione_standard(df):
    print("La deviazione standard dell'età:")
    print(df["Età"].var())
    print("La deviaziane standard del Salario:")
    print(df["Salario"].var())

def rimuovi(df):
    duplicati = df.drop_duplicates()
    return duplicati

def sostituire(df):
    df['Età'].fillna(df['Età'].median(), inplace=True)
    df['Salario'].fillna(df['Salario'].median(), inplace=True)



def salva(df):
    df.to_csv("esercizio_dataframe_1.csv")


def menù():
    controllo = True
    while controllo:
        print("Menù")
        print("Crea una DataFrame (1) ")
        print("Stampa le prime 5 e le ultime 5 righe (2) ")
        print("stampa il tipo di dato (3) ")
        print("Rimuovi i duplicati (4) ")
        print("Media (5) ")
        print("Mediana (6)")
        print("Deviazione standard (7)")
        print("Sostituire i valore mancanti con la mediana (8)")
        print("Salvare in un file csv (9)")
        print("Exit (10) ")
        utente = input("Inserisci l'operazione da fare: ")

        df = data_frame()
        prime = prime_ultime_righe(df)
        tipo = tipo_dati(df)
        duplicati = rimuovi(df)
        media_data = media(df)
        mediana_data = mediana(df)
        deviazione_data = deviazione_standard(df)
        salvataggio = salva(df)

        if utente == "1":
            print(df)
        elif utente == "2":
            print(prime)
        elif utente == "3":
            print(tipo)
        elif utente == "4":
            print(duplicati)
        elif utente == "5":
            print(media_data)
        elif utente == "6":
            print(mediana_data)
        elif utente == "7":
            print(deviazione_data)
        elif utente == "9":
            print(salvataggio)
        else:
            break

menù()
