#esercizio funzioni.1
def indovina():                                           #funzione indovina
    numero_da_indovinare=10                                      #condizione
    controllo=True
    numero=0
    while controllo:
        print("Indovina il numero compreso da 1 a 100!")
        utente=int(input("inserisci un numero: "))              #inserimento numero dall'utente

        if utente == numero_da_indovinare:
            print("Complimenti!")                               #stampa se il numero è uguale a quello preinpostato
        
            break                                               #termina il ciclo

        elif utente < numero_da_indovinare:                     #controlla se il numero è minore
            print("Il numero è più basso")
            
        
        elif utente > numero_da_indovinare:                     #controlla se il numero è maggiore
            print("Il numero è più alto")
            

indovina(20)                        #chiamata funzione
    