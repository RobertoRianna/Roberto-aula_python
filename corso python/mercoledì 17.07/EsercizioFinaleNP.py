import numpy as np


def crea():                                                     #crea la matrice inserendo in input righe e colonne
    righe = int(input("Inserisci le righe: "))
    colonne = int(input("Inserire le colonne: "))               
    matrice2D = np.random.randint(righe,colonne)
    return matrice2D, righe, colonne
    
def sotto_matrice(matrice2D,righe,colonne):
    matrice_sotto = matrice2D[1:righe-1,1:colonne-1]           #dalla prima riga alla penultima e dalla prima colonna alla penultima
    return matrice_sotto

def trasporre(matrice2D):
    matrice_trasposta = np.transpose(matrice2D)                 #trasporre la matrice con la funzione trasponse
    return matrice_trasposta

def somma(matrice2D):                                           #somma della matrice
    somma_matrice = np.sum(matrice2D)
    return somma_matrice

def moltiplicazione(matrice2D,righe,colonne):                               #moltiplicazione 
    matrice3=np.random.randint(righe,colonne)
    prodotto = matrice2D * matrice3                                          #prodotto degli elementi uno per volta
    return matrice3, prodotto

def media(matrice2D):
    media_matrice = np.mean(matrice2D)                                      #media
    return media_matrice

def matrice_inversa(matrice2D):
    matrice2_inversa = np.linalg.inv(matrice2D)                             #calcola matrice inversa
    return matrice2_inversa

def funzioni_matematiche(matrice2D):                                        #calcola l'esponente della matrice
    esponenziale = np.exp(matrice2D[matrice2D>0])
    return esponenziale

def valore_maggiore(matrice2D):
    elementi_maggiori = matrice2D[matrice2D > 2]                            #visualizza gli elementi maggiori di 2
    return elementi_maggiori




def menù():
    controllo = True
    while controllo:
        print("Menù")
        print("Crea una matrice (1) ")
        print("Stampa sotto-matrice centrale (2) ")
        print("Trasporre la matrice (3) ")
        print("Somma di tutti gli elementi (4) ")
        print("Moltiplicare elemento per elemento un nuovo array (5) ")
        print("Media della matrice (6) ")
        print("Calcolo matrice inversa: (7) ")
        print("Calcolo esponenziale (8) ")
        print("Calcolo elemnti mggiore di 2: (9) ")
        print("Exit (10) ")
        utente = input("Inserisci l'operazione da fare: ")

        matrice2D,righe,colonne = crea()
        matrice_sotto = sotto_matrice(matrice2D,righe,colonne)
        matrice_trasposta = trasporre(matrice2D)
        somma_matrice = somma(matrice2D)
        prodotto = moltiplicazione(matrice2D,righe,colonne)
        media_matrice = media(matrice2D)
        matrice2_inversa = matrice_inversa(matrice2D)
        esponenziale = funzioni_matematiche(matrice2D)
        elementi_maggiori = valore_maggiore(matrice2D)

        if utente == "1":
            print(matrice2D)
        elif utente == "2":
            print(matrice_sotto)
        elif utente == "3":
            print(matrice_trasposta)
        elif utente == "4":
            print(somma_matrice)
        elif utente == "5":
            print(prodotto)
        elif utente == "6":
            print(media_matrice)
        elif utente == "7":
            print(matrice2_inversa)
        elif utente == "8":
            print(esponenziale)
        elif utente == "9":
            elementi_maggiori
        else:
            break

menù()





















    







