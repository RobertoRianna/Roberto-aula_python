#Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti, quando l’utente scrive media il programma
#andrà a stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti.
#Esempio:
#Nome: Giovanni , Media: 7.5
#Nome: Alfredo , Media: 9
#Nome: Michela, Media 10

studenti = {}

while True:
    comando = input("Inserisci il nome Studente o 'Media' per conoscere le medie dei voti: ")
    if comando.lower() == "media":
    #media
        if len(studenti)== 0:
            print("Nessun alunno presente")
        else:
            break
    else:
        #aggiungi nomi e voti
        studenti[comando] = []
        Nvoti = input("Quanti voti vuoi inserire? ")
for num in range(int(Nvoti)):
    voto = input("Inserisci il voto: ")
    studenti[comando].append(int(voto))

studenti = {'Tommaso': [7, 10], 'Giovanni': [10, 6, 7]}
print(studenti)

for studente in studenti:
    if len(studenti[studente]) == 0:
        print(f"Nome: {studente}, Media: {0}")
else:
    media = sum(studenti[studente]) /len(studenti[studente])
    print(f"Nome: {studente}, Media: {media}")

