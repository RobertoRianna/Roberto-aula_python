#Utilizzate la linear regression per analizzare il dataframe di esempio con Fabbisogno calorico giornaliero di un uomo in base alla sua età, 
# allenate l'algoritmo, testatelo e poi realizzate un grafico.

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



    
def leggi_df():
    df = pd.read_csv("C:\\Users\\Roberto Rianna\\Desktop\\giovedì 25.07\\fabbisogno_calorico.csv")
    return df

def regressione_lineare(df):
    X = df[["età"]]
    y = df["calories"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = LinearRegression()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(f"Coefficiente: {model.coef_}")
    print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
    print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
    plt.scatter(X_test, y_test)
    plt.plot(X_test,y_pred)

    plt.xticks(())
    plt.yticks(())

    plt.show()


df = leggi_df()
regressione_lineare(df)