#Scrivere un programma Python che scarica l’xml della home page ANSA e stampa tutte le informazioni della prima notizia.

import requests 
import xml.etree.ElementTree as ET

contenuto = requests.get("https://www.ansa.it/sito/ansait_rss.xml").text
root = ET.fromstring(contenuto)

channel = root.find("channel")
notizia = channel.find("item")
titolo = notizia.find("title")


print(titolo.text)