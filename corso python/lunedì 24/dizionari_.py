utente1={"nome": "tommaso","cognome":"muraca","età":37}
print(utente1["età"])                                           #stampa età



utente1={"nome": "tommaso","cognome":"muraca","età":37}

print(utente1.get("nome"))                                     #stampa tutto
print(utente1.get("indirizzo","nessun indirizzo"))             #stampa nessun indirizzo

utente1["indirizzo"]="via rossi"                                #ha aggiunto al dizionario indirizzo e il suo valore

for element in utente1.values():                                #stampa tutti i valori
    print(element)

print(utente1.setdefault("Indirizzo","nessun valore"))          #stampa e ppoi aggiunge indirizzo eil valore al dizionario

lista=(utente1.items())                                              #stampa tutto sia chiavi che valori

for indice, valore in enumerate(lista):
    print(f"indice{indice}, valore{valore}")                        #stampa indici e valori di qualsiasi funzione(non solo dizionari)
