import pandas as pd
#creazione di un datafframe con dati di esempio
data = {
    'nome': ['alice','bob','carla'],
    'età': [25,30,22],
    'città':['roma','milano','napoli']
}
df = pd.DataFrame(data)

#stampa del dataframe originale
print("data frame originale: ")
print(df)
#selezione delle righe dove l'età è superiore a 23
df_older = df[df['età']>23]
#stampa delle righe selezionate
print("erone con età superipre a 23 anni: ")
print(df_older)
#aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['età'] >= 18
#stampa del dataframe con la nuova colonna
print("dataframe con colonna 'maggiorenne' ")
print(df)