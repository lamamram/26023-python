# %%
"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. renommer le fichier csv en dns.csv
4.. ne faire ce qui précède qui si ce n'est pas déjà fait


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""
# %%
import requests
import os

URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
zip_name = "202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"

# on télécharge si le fihier n'existe pas
if not os.path.exists(zip_name):
    # téléchargement avec le verbe get http
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            if ("Content-Type" in response.headers 
                and "zip" in response.headers["Content-Type"]):
                with open(zip_name, "wb") as f:
                    f.write(response.content)
        elif response.status_code == 404:
            raise ValueError(f"fichier introuvable à cette {URL.split('/')[-1]}")
    except (requests.exceptions.ConnectionError, ValueError) as e:
        print(e)
            


# %%
from zipfile import ZipFile

# ouvrir le zip pour extraire le csv et le renommer
if not os.path.exists("dns.csv"):
    with ZipFile(zip_name, mode="r") as zf:
        items = zf.namelist()
        zf.extract(items[0])
        os.rename(items[0], "dns.csv")

# %%
import csv

NB_SLICES = 2
NB_LINES = 100000

with open("dns.csv", "r", encoding="utf-8") as rf:
  reader = csv.reader(rf, delimiter=";")
  
  header = next(reader)
  rows = []

  for i, row in enumerate(reader, start=1):
    if i > NB_LINES * NB_SLICES: break

    rows.append(row)
    
    ## SI je ne suis pas sur une ligne de découpage, (multiple de NB_LINES)
    ## ALORS j'arrête l'itération courante
    ## ET je continue avec la suivante
    if i % NB_LINES: continue  

    with open(f"dns_{i}.csv", "w", encoding="utf-8", newline="") as wf:
        writer = csv.writer(
            wf,
            delimiter=";"
        )
        writer.writerow(header)
        writer.writerows(rows)
        # rows = []
        rows.clear()