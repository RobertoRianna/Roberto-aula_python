import pandas as pd

#percorso del file csv
file_path = 'vendite.csv'
#caricamento dei dati nel dataframe
df = pd.read_csv(file_path)
#le prime righe del Dataframe per confermare
print(df.head())


