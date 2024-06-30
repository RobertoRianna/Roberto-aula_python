from random import randint              #importa la funzione e ci da un valore random
randint()


from random import randint              #ci da un numero casuale da 1 a 100
print(randint(1,100))


from random import random               #valore casuale da 0 a 1
print(random())


from random import randrange            #numero casuali da 1 a 100 con step(intervallo) di 3 numeri(ogni 3 numeri)
print(randrange(1,100,3))


from random import choice               #ci da un valore random che è presente nella lista
lista=["uno","due","tre","quattro"]
print(choice(lista))


from datetime import date               #si usa per le date
print(type(date(2024,6,25)))


from datetime import datetime           #ci da la data di oggi
print(datetime.now())


from time import sleep                  #ferma il codice per 20 secondi
print("prima dello sleep")
sleep(20)
print("Dopo dello sleep")


print("avvio programma")                #si usa per gli errori, se è sbagliato il primo comando stampa il secondo
try:
    print(int("Ciao"))
except:
    print("errore")
print("continuo programma")


