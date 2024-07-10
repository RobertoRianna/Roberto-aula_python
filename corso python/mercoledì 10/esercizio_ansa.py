#Scaricare l’RSS di ANSA Ultime Notizie e convertirlo in un file CSV e un file html.

import pandas as pd
import xml.etree.ElementTree as ET

import requests 

contenuto = requests.get("https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml").text
root = ET.fromstring(contenuto)


df_col = ["title", "link","description","language","copyright"]

righe = []

for nodo in root:
    title = nodo.find("title").text if nodo is not None else None
    link = nodo.find("link").text if nodo is not None else None
    description = nodo.find("description").text if nodo is not None else None
    language = nodo.find("language").text if nodo is not None else None
    copyright = nodo.find("copyright").text if nodo is not None else None

    righe.append({"title":title, "link":link, "description": description, "language": language, "copyright": copyright})

#print(righe)

df = pd.DataFrame(righe, columns=df_col)

print(df)


df.to_csv("notizie.csv", index=False)

df = pd.read_csv("notizie.csv")

df.to_html("notizie.html", index=False)