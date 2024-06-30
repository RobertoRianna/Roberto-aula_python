

stringa= "ciao a tutti"
len(stringa)                        #lunghezza stringa
print(stringa.endswith("tti"))   #controlla se la stringa finisce con ..
print(stringa.startswith("i"))   #controlla se inizia con ...
print(stringa.isalpha())         #controlla se la stringa contiene caratteri alphanumerici
print(stringa.isdecimal())       #controlla se ha caratteri decimali
print(stringa.isspace())         #controlla se ci sono degli spazi


stringa="ciao"
stringa=stringa.replace("ci", " ")    #sostituisce "ci" con lo spazio vuoto
print(stringa)

stringa=stringa.count("c")            #conta quante "c" ci sono nella stringa

lista=stringa.split(" ")              #divide le parole della lista



lista=["ciao","a","tutti"]
separatore="\n"
stringa=separatore.join(lista)             #separa la lista
print(lista)



lista=["ciao","a","tutti"]
stringa2=lista[:4]                          #stampa fino al quarto carattere
print(stringa2)





frutta = ["mela", "pera", "banana", "ciliegia"]
frutta_e=[]
for frutto in frutta:
    if "e" in frutto:  
        frutta_e.append(frutto)      #stampa solo le parole con le lettere "e"
print(frutta_e)



