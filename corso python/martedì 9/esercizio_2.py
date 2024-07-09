# Scrivere un programma Python che crea un documento XML basato su dati forniti. 
# Ad esempio, considera il seguente elenco di studenti:
# studenti = [
# {'nome': 'Alice', 'eta': '22'},
# {'nome': 'Bob', 'eta': '25'},
# {'nome': 'Charlie', 'eta': '20'}
# ]
# Il programma dovrebbe creare un documento XML che rappresenti questi studenti.
# Infine esportatelo come file.

import xml.etree.ElementTree as ET

studenti = [
 {'nome': 'Alice', 'eta': '22'},
 {'nome': 'Bob', 'eta': '25'},
 {'nome': 'Charlie', 'eta': '20'}
 ]

root = ET.Element("studenti")
counter = 1
for studente_r in studenti:
    tag_studente = ET.Element("studente", {"id": str(counter)})
    for chiave,valore in studente_r.items():
        tag = ET.Element(chiave)
        tag.text=studente_r[chiave]
        tag_studente.append(tag)

    root.append(tag_studente)
    counter +=1

tree = ET.ElementTree(root)
tree.write("studente.xml")







