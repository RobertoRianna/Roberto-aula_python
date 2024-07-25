#Partendo dal dataset a questo link https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression ,
# utilizzate i dati sulle ore di studio e le ore di sonno per prevedere quanto queste caratteristiche influiscono 
# sull'indice di prestazione degli studenti.

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def leggi():
    df = pd.read_csv("C:\\Users\\Roberto Rianna\\Desktop\\giovedì 25.07\\Student_Performance.csv")
    return df
    
def regressione_lineare(df):
    X = df[["Hours Studied","Sleep Hours"]]
    y = df["Performance Index"]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    model = LinearRegression()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(f"Coefficiente: {model.coef_}")
    print(f"Errore quadratico medio: {mean_squared_error(y_test,y_pred)}")
    print(f"Coefficiente di determinazione: {r2_score(y_test,y_pred)}")
    print(f"Predizioni:\n{y_pred}")

    plt.subplot(2,1,1)
    plt.scatter(X_test["Hours Studied"], y_test)
    plt.plot(X_test["Hours Studied"],y_pred)
    plt.title("Regressione lineare ore di studio/indice di performance")
    plt.xticks(())
    plt.yticks(())

    plt.subplot(2,1,2)
    plt.scatter(X_test["Sleep Hours"], y_test)
    plt.plot(X_test["Sleep Hours"],y_pred)
    plt.title("Regressione lineare ore di sonno/indice di performance")

    plt.xticks(())
    plt.yticks(())
    plt.show()


df = leggi()
regressione_lineare(df)






