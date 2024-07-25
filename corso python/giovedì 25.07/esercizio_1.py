#Utilizzate la linear regression per analizzare il dataframe di esempio in cui abbiamo le Calorie bruciate 
# in base al peso della persona che fa esercizio fisico con la montain bike, allenate l'algoritmo, 
# testatelo e poi realizzate un grafico



import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



    
def leggi_df():
    df = pd.read_csv("C:\\Users\\Roberto Rianna\\Desktop\\giovedì 25.07\\calories.csv")
    return df
def regressione_lineare(df):
    X = df[["kg"]]
    y = df["calories"]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    modello = LinearRegression()
    modello.fit(X_train,y_train)
    y_pred = modello.predict(X_test)
    (f"Coefficiente: {modello.coef_}")
    print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
    print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
    plt.scatter(X_test, y_test)
    plt.plot(X_test,y_pred)

    plt.xticks(())
    plt.yticks(())

    plt.show()

        


df = leggi_df()
regressione_lineare(df)


