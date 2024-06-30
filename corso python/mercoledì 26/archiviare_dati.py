dizionario_alunni = {"tommaso":[10,7,8]}

with open("file2.csv","r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")
diz_alu2 = {}
for element in righe:
    celle = element.split(",")                                  #archiviare
    diz_alu2[celle[0]] = []
for voti in celle[1].split("-"):
    diz_alu2[celle[0]].append(voti)

print(diz_alu2)



#..............................................

dizionario_alunni = {"tommaso":[10,7,8]}

with open("file2.txt","r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")

#print(righe)                                                                       #ARCHIVIARE
diz_alu2 ={}
for riga in righe:
    elemento = riga.split(",")
    #print(elemento)
diz_alu2[elemento[0]] =[]
for voto in range(1,len(elemento)):
    diz_alu2[elemento[0]].append(elemento[voto])
    print(diz_alu2)

#------------------------------

nome = "tommaso"

voti = "6 10 7"

lista_voti = voti.split(" ")


                                                                                        #archiviare
stringa_voti_archiviati = "-".join(lista_voti)

#print(stringa_voti_archiviati)

stringa_alunno = nome+","+stringa_voti_archiviati

print(stringa_alunno)

#------------------------------------

{"tommaso":[7,6,8],"giuseppe":[7,5,10]}

with open("file2.txt","r") as file:
    contenuto = file.read()

inutili = ["[","]","{","}","\""]

for element in inutili:
    contenuto = contenuto.replace(element,"")

contenuto = contenuto.replace(":",",")                                                                  #archivio e pulizia del dizionario

lista = contenuto.split(",")
#{"tommaso":[7,6,8],"giuseppe":[7,5,10]}

#['tommaso', '7', '6', '8', 'giuseppe', '7', '5', '10']

dizionario = {}
for elemento in lista:
    if elemento.isalpha():
        dizionario[elemento]= []
        nome = elemento
    else:
        dizionario[nome].append(int(elemento))

print(dizionario)