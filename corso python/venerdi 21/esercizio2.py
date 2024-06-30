#Chieda all'utente di inserire un numero intero positivo n.
#Se il numero inserito non è positivo, chieda nuovamente l'inserimento fino a quando non viene inserito un numero positivo.
#Una volta ottenuto un numero positivo n, il programma dovrà:
#Stampare tutti i numeri pari da 0 a n inclusi.
#Calcolare e stampare la somma di tutti i numeri dispari da 0 a n inclusi.
#terminare solo dopo tre tentativi ("hai finito i tentativi") o dopo che una soma totale supera 250 ("hai vinto")

controllo= True
while controllo:
    numero=int(input("Inserisci un numero intero positivo?"))
    if numero >0:
         for i in range(0, numero):     #visualizza i numeri da 0 a n
              if i%2 ==0:                   #controlla se il numero è pari
                   print(i)             #stampa i numeri pari da 0 a n
         break
                              
                         
    elif numero <0:
         print("Inserisci un numero positivo: ")



