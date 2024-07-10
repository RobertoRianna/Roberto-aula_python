# Creare un dataframe e stamparlo avendo come fonte l’XML utilizzato per l’esercizio sui libri:
# <libri>
# <libro>
# <titolo>Python Cookbook</titolo>
# <autore>David Beazley</autore>
# </libro>
# <libro>
# <titolo>Fluent Python</titolo>
# <autore>Luciano Ramalho</autore>
# </libro>
# </libri>
#esportatelo in csv e html

import pandas as pd
import xml.etree.ElementTree as ET

xml = """<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>"""

root = ET.fromstring(xml)

df_col = ["titolo", "autore"]

righe = []

for nodo in root:
    titolo = nodo.find("titolo").text if nodo is not None else None
    autore = nodo.find("autore").text if nodo is not None else None
    

    righe.append({"titolo":titolo, "autore":autore})

#print(righe)

df = pd.DataFrame(righe, columns=df_col)

print(df)


df.to_csv("libri.csv", index=False)

df = pd.read_csv("libri.csv")

df.to_html("libri.html", index=False)