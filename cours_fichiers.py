# %%
# création / écrasement du fichier data.txt
f = open("data.txt", "w", encoding="utf-8")
f.write("1ère ligne\n")
f.write("2nde ligne\n")
f.close()
# %%

# gestionnaire de contexte: ouverture / fermeture
with open("data.txt", "w", encoding="utf-8") as f:
  f.write("1ère ligne\n")
  f.write("2nde ligne\n")
# le close est exécuté auto. en sortant du bloc with
# %%

## lecture
# f.read() => lit tout le contenu du fichier
# f.read(n) => lit n caractères lié à l'encodage du fichier
# f.seek(pos) => positionne le curseur à la position pos (en OCTETS)
with open("data.txt", "r", encoding="utf-8") as f:
  # je lis à la fin de la 1ère ligne sans saut deligne (ici \n)
  first_row = f.read(10)
  f.seek(12)
  second_row = f.read(10)
# print: ajoute un \n à la fin de ce qu'on lui donne à afficher
print(first_row)
print(second_row)

# %%
## attention avec seek
with open("data.txt", "r", encoding="utf-8") as f:
  # je positionne le curseur sur le 2ème octet du fichier
  # => au milieu du caractère "è" qui est codé sur 2 octets en utf-8
  f.seek(2)
  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 2: invalid continuation byte
  print(f.read())

# %%

# a comme append => ajoute du contenu à la fin du fichier
with open("data.txt", "a", encoding="utf-8") as f:
  f.write("3ème ligne\n")

# %%
# un fichier est un itérable

with open("data.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line, end="") # end="" => ne pas ajouter de saut de ligne après chaque ligne lue
# %%
## écriture d'un csv
import csv

# csv.reader() # pour lire un csv
# csv.writer() # pour écrire dans un csv

users = [
  {"id": 1, "first_name": "Jean", "last_name": "Dupont", "age": 30, "comment": "blabla; blabla"},
  {"id": 2, "first_name": "Marie", "last_name": "Curie", "age": 25, "comment": "blabliblo"},
]

# newline="" => ne pas ajouter de ligne vide entre chaque ligne écrite dans le csv avec Windows
with open("data.csv", "w", encoding="utf-8", newline="") as f:
  # quotechar='"' => les champs contenant des caractères spéciaux (ex: ;) sont entourés de guillemets
  # quoting=csv.QUOTE_MINIMAL => n'entoure que les champs qui en ont besoin
  writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
  header = users[0].keys()
  writer.writerow(header)
  for user in users:
    writer.writerow(user.values())
  
  ## option B: transfotmat° d'une liste de dicts en une liste de listes de valeurs
  # records = list(map(lambda user: list(user.values()), users))
  # writer.writerows(records)


# %%
