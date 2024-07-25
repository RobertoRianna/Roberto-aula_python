#Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction , 
# utilizzate i dati sugli anni delle case e la distanza dalla stazione metro per prevedere quanto queste caratteristiche
# influiscono sul costo delle case.

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay


def leggi_df():
    df = pd.read_csv("C:\\Users\\Roberto Rianna\\Desktop\\giovedì 25.07\\Real estate.csv")
    return df

def regressione_lineare(df):
    X = df[["X2 house age","X3 distance to the nearest MRT station"]]
    y = df["Y house price of unit area"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    model = LinearRegression()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(f"Coefficiente: {model.coef_}")
    print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
    print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
    display = PredictionErrorDisplay(y_true=y_test, y_pred=y_pred)
    display.plot()
    plt.show()
    plt.subplot(2,1,1)
    plt.scatter(X_test["X2 house age"], y_test)
    plt.plot(X_test["X2 house age"],y_pred)
    plt.title("Regressione lineare età case/prezzo case")
    plt.xticks(())
    plt.yticks(())

    plt.subplot(2,1,2)
    plt.scatter(X_test["X3 distance to the nearest MRT station"], y_test)
    plt.plot(X_test["X3 distance to the nearest MRT station"],y_pred)
    plt.title("Regressione lineare distanza dalla stazione/prezzo case")

    plt.xticks(())
    plt.yticks(())
    plt.show()

df = leggi_df()
regressione_lineare(df)

