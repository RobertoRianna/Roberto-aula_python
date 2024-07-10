import requests 

contenuto = requests.get("https://www.ansa.it/sito/notizie/sport/calcio/calcio_rss.xml")

print(contenuto.text)