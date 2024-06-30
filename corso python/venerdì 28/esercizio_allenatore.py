#Create un gestionale per la vostra squadra di calcio, siete gli allenatori quindi potete aggiungere massimo 25 calciatori:
#- 3 portieri;
#- 8 difensori;
#- 8 centrocampisti;
#- 6 attaccanti;
#per ogni calciatore nome e ruolo.
#Nel menù potete aggiungerli, eliminarli o visualizzarli, tutto verrà salvato in un database .txt o .csv

def verifica_ruolo(scelta_ruolo):
    lista=[0,0,0,0]
    if db_vuoto:
      return True
    else:
        if len(db)>1:
            righe=db.split("\n")
            for riga in righe:
                riga=riga.split(",")                            
                if riga[0]=="Portiere":
                    lista[0]+=1
                elif riga[0]=="Difensore":
                    lista[1]+=1
                elif riga[0]=="Centrocampista":
                    lista[2]+=1
                else:
                    lista[3]+=1
        if scelta_ruolo == "1":
            if lista[0] <3:
                return True
            else:
                return False
        elif scelta_ruolo == "2":
            if lista[1] <8:
                return True
            else:
                return False
        elif scelta_ruolo == "3":
            if lista[2] <8:
                return True
            else:
                return False
        else:
            if lista[3] <6:
                return True
            else:
                return False



def scrittura(s,mod):
    with open("venerdì 28\file.csv",mod) as file:
        file.write(s)

def lettura():
    with open("venerdì 28\file.csv","r") as file:
        dato=file.read()
    return   dato


def verifica_db():
    db_vuoto=True
    try:
        db=lettura()
    except :
        db=scrittura("","w")
    if len(db)>0:
        db_vuoto=False
    return db,db_vuoto

db,db_vuoto= verifica_db()

def aggiungi():
    scelta_ruolo=input("1 per portiere, 2 per difensore, 3 centrocampista, 4 attacante")
    if scelta_ruolo== "1":
        if verifica_ruolo(scelta_ruolo):
            nome=input("inidca il nome del calciatore")
            dato="Portiere"+","+nome+"\n"
            scrittura(dato,"a")
        else:
            print("Superato limite")
    elif scelta_ruolo== "2":
        if verifica_ruolo(scelta_ruolo):
            nome=input("inidca il nome del calciatore")
            dato="Difensore"+","+nome+"\n"
            scrittura(dato,"a")
        else:
            print("Superato limite")
    elif scelta_ruolo== "3":
        if verifica_ruolo(scelta_ruolo):
            nome=input("inidca il nome del calciatore")
            dato="Centrocampista"+","+nome+"\n"
            scrittura(dato,"a")
        else:
            print("Superato limite")
    elif scelta_ruolo== "4":
        if verifica_ruolo(scelta_ruolo):
            nome=input("inidca il nome del calciatore")
            dato="Attaccante"+","+nome+"\n"
            scrittura(dato,"a")
        else:
            print("Superato limite")
    else:
        print("valore non valido")

def visualizza_rosa():
    if db_vuoto:
        print("Non c'è nessun giocatore in rosa")
    else:
        if len(db) >1:
            righe = db.split("\n")
            for riga in righe:
                riga = riga.split(",")
                

def menu():
    print("Benvenuto allenatore!")
    print("Inserire calciatore: 1")
    print("Visualizza squadra: 2")
    print("Exit: 3")


while True:
    menu()
    a = input("Indicare scelta: ")
    if a == "1":
        aggiungi()
    elif a == "2":
        pass
    elif a == "3":
        print("Arrivederci")
        break
    else:
        print("Non valido")