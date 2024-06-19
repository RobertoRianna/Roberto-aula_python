#dizionario
studente={
    "nome": "Alice",
    "età": 20,
    "sesso":"femmina"
}
print(studente["nome"])
print(studente["età"])

#modifica valore dizionario
studente ["età"]=21
print(studente)

#dizionario funzioni
studente={
    "nome": "Alice",
    "età": 20,
    "sesso":"femmina"
}
print(studente.keys())
print(studente.values())
print(studente.items())
print(studente.get("nome"))