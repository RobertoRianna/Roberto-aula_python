def indovina(numero):
    numero_da_indovinare=10
    controllo=True
    while controllo:
        print("Indovina il numero compreso da 1 a 100!")
        utente=int(input("inserisci un numero: "))

        if utente == numero_da_indovinare:
            print("Complimenti!")
            break

        elif utente < numero_da_indovinare:
            print("Il numero è più basso")
            
        
        elif utente > numero_da_indovinare:
            print("Il numero è più alto")
            

indovina("Il numero è il 10, Complimenti!")
    