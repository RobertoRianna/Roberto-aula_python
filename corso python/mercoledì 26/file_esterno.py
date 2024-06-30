with open("file.csv","r") as file:                  #legge e apre un file esterno
    print(file.read())                              


with open("text.txt","x") as file:                  #crea un file
    pass

with open("text.txt","a") as file:                 #crea un file e scrive ciao se è già esistente il file
    file.write("ciao")

with open("text.txt", "w") as file:                 #se il file non esiste lo crea e scrive ciao se esiste già cancella quello che c'è e scrive ciao
    file.write("ciao")

with open("test.txt","r") as file:                  #legge tutte le righe del file e crea una lista per tutte le righe
    contenuto=file.readlines()
print(contenuto)


with open("file.csv","r") as file:                  #stampa tutto il file
    contenuto=file.read( )


with open("file.csv","r") as file:
    contenuto=file.read()
righe=contenuto.split("\n")                     #divide le righe
print(righe)


with open("file.csv","r") as file:
    contenuto=file.read()
righe=contenuto.split("\n")                     #divide le righe
for element in righe:
    print(element.split(",")[0])                #stampa la prima riga


with open("file.csv","r") as file:
    contenuto=file.read()
righe=contenuto.split("\n")                     #divide le righe
elemnti=[]
for element in righe:
    elemnti.append(element.split(","))          #crea 3 liste
    print(element)

