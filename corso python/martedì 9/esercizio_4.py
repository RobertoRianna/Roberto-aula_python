# Scrivere un programma Python che ricerca e stampa gli elementi di un documento XML che soddisfano determinati criteri. 
# Considera il seguente documento XML:
# <prodotti>
# <prodotto>
# <nome>Laptop</nome>
# <prezzo>800</prezzo>
# </prodotto>
# <prodotto>
# <nome>Smartphone</nome>
# <prezzo>500</prezzo>
# </prodotto>
# <prodotto>
# <nome>Tablet</nome>
# <prezzo>300</prezzo>
# </prodotto>
# </prodotti>
# Il programma dovrebbe cercare e stampare tutti i prodotti con un prezzo inferiore a 600.

import xml.etree.ElementTree as ET

dati = """<prodotti>
<prodotto>
<nome>Laptop</nome>
<prezzo>800</prezzo>
</prodotto>
<prodotto>
<nome>Smartphone</nome>
<prezzo>500</prezzo>
</prodotto>
<prodotto>
<nome>Tablet</nome>
<prezzo>300</prezzo>
</prodotto>
</prodotti>"""

root = ET.fromstring(dati)

for prodotto in root.findall('prodotto'):
    prezzo = int(prodotto.find('prezzo').text)
    if prezzo < 600:
        nome = prodotto.find('nome').text
        print(nome,prezzo)