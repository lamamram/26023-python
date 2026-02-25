# %%
# module standard: pas besoin d'utiliser pip
import json
# module tiers: installé à partir de pip, dans l'environnement virtuel

user_data = {
  "name": "John Doe",
  "age": 30,
  "email": "john@example.com"
}

# sérialiaser en json
# json_string = json.dumps(user_data)
# print(json_string, type(json_string))

# %%
import requests

response = requests.get("https://www.dawan.fr/")

print(f"""
      code de réponse de l'url : {response.status_code}
      url fonctionnelle ? { 200 <= response.status_code < 300 }
""")

# contenu de type 'page html' donc texte
if "text/html" in response.headers["Content-Type"]:
  print(response.text)

# %%
# gestion des paramètres d'une fonction
## paramètres positionnels: appelés de manière nommée

def substr(x: int, y: int) -> int:
  return x - y

print(substr(2, 3))
print(substr(3, 2))
# les annotations sont informatives, pas de contrôle de type
print(substr.__annotations__)
# TypeError: print(substr("machin", 2))

# les valeurs de paramètre sont fléchées
print(substr(y=2, x=3))

# %%
from functools import reduce

# gestion des paramètres d'une fonction
## paramètres "variadics" positionnels: *args


# je veux sommer un nb indéfini de nombres
def sum_all(*truc: float) -> float:
  print(truc)
  return reduce(lambda acc, x: acc + x, truc)

print(sum_all(1, 2, 3))

# %%

from datetime import datetime
import re

# gestion des paramètres d'une fonction
## paramètres "variadics" nommés: **kwargs

def create_user(name: str, date_birth: str, **opts):
  """
  fonction de création d'utilisateur
  name: nom de l'utilisateur
  date_birth: date de naissance de l'utilisateur
  opts: options supplémentaires
    - email
    - age
    ...
  """
  dt = datetime.strptime(date_birth, "%Y-%m-%d")
  # partie obligatoire
  user = {
    "name": name,
    "date_birth": dt.strftime("%Y-%m-%d")
  }
  # r"" : raw string, pour ne pas devoir échapper les caractères spéciaux
  # [^@]: tout caractère sauf @
  # + : un ou plusieurs caractères
  # \. : le caractère . car "." signifie n'importe quel caractère en regex
  if "email" in opts:
    if re.match(r"[^@]+@[^@]+\.[^@]+", opts["email"]):
      user["email"] = opts["email"]
    else:
      raise ValueError(f"email {opts['email']} non valide")
  return user

try:
  print(create_user("John Doe", "1981-05-22"))
  print(create_user("John Doe", "1981-05-22", email="joe@example.com", truc="machin"))
except ValueError as e:
  print(f"Erreur: {e}")

# %%
## utilisation de * et ** à l'appel d'une fonction

parameters = ["John Doe", "1981-05-22"]
print(create_user(parameters[0], parameters[1]))
# injecter les éléments de la liste 
# dans les paramètres positionnels de la fonction
print(create_user(*parameters))

kwds = {"name": "John Doe", "date_birth": "1981-05-22"}
# les clés du dictionnaire doivent correspondre aux noms des paramètres de la fonction
print(create_user(**kwds))

# %%
# instruction vs expression

## une expression est une construction syntaxique qui retourne une valeur
## peut être mis en paramètre dans print => évaluable

## valeur littérale | variable | appel de fonction | expression conditionnelle | expression lambda | combinaison de ces éléments
x = 5
def add(a, b):
  return a + b
print(5, x, x + 5, "machin".upper(), add(2, 3))

# TypeError print(x = 5)
# SyntaxError print(if x < 5: x = 2)
# %%

# transformations réciproque str <=> list, tuple

target = "le petit chat est mort"
words = target.split()

" ".join(words)

# %%

# transformer une chaine de caractère <=> tableau d'octet (sans encodage)

target = "ma chaine"
octets = bytes(target, "utf8")
octets.decode("utf8")

# %%
# possible pour les caractère ascii
# ASCII: caractère de base a-zA-Z0-9,;:!... (255 caractères)
# il sont encodé sur UN SEUL OCTET 
octets = b"ma chaine"

# pour voir les codes ascii <=> lettres
ord("a"), chr(97)
# %%

## n'importe quelle EXPRESSION peut utiliser les attributs d'un type ou d'une classe

# valeurs litérales

"bonjour".upper()

# variables
mot = "bonjour"
mot.upper()

# expression qui retourne un str

print((mot + " les gens").upper())

print(mot[2:4].upper())

# %%

# valeurs booléennes de chaque type
# 0, 0., "", [], (), {}
x = ()
if x:
  print("vrai")
else:
  print("faux")

# %%

# int, float str, tuple => immutable

immutable = "bonjour"
# impossible car immutable
# immutable[0] = "B"
# capitalize => retourne la valeur avec B 
# MAIS ne modifie la chaine de caractère
# DONC il faut réaffecter la trasformat° dans la var
immutable = immutable.capitalize()
print(f"transformation immutable: {immutable}")

# list, dict => mutable

mutable = [-1, 2, 3]
# remplacer -1 par 1 => je modifie un élément de la liste, 
# sans réaffecter la liste elle même
mutable[0] = 1
print(f"transformation mutable: {mutable}")

# %%
## souvent les fonctions sur les mutables (list, dict)
# ne retournent RIEN car elles modifient directement la variable

## les fonctions sur les immutables retourent TOUJOURS qqch
# PUISQUE elles ne peuvent pas modifier directement la variable

print(mutable.append(4))
print(mutable)


# %%
## gérer une clé inexistante dans un dict

user = {"name": "matt", "age": 43} #, "email": "mlamamra@dawan.fr"}
# print(user["email"]) => KeyError


print("name" in user)
# option A: avec l'opérateur in => fonctionne avec les clés
if "email" in user:
  print(user["email"])
else:
  print("rh@dawan.fr")

# option B: la fonction get demande la valeur de la clé (s'il existe) OU une valeur par défaut
print(user.get("email", "rh@dawan.fr"))

# %%
