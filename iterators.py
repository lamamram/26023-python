# %%
# exemple d'itérable custom: MyRange
class MyRange:
  def __init__(self, limit=10):
    # condition d'arrêt de l'itération
    self.limit = limit
  
  def __iter__(self):
    # (re)initialisation du compteur
    self.counter = 0
    return self
  
  def __next__(self):
    if self.counter < self.limit:
      # on retourne la valeur courante du compteur
      current = self.counter
      # on incrémente le compteur pour la prochaine itération
      self.counter += 1
      return current
    else:
      # on signale la fin de l'itération
      raise StopIteration

# for capture l'exception StopIteration
mr5 = MyRange(5)
# print(mr5.counter)
print("="*50)

# le premier for génère le counter
for i in mr5:
  print(i)

print("="*50)

# le 2ème for remet counter à 0
for i in mr5:
  print(i)
# %%
# itération manuelle

# génère un itérable
mr5 = MyRange(5)

# génère un itérateur à partir de l'itérable
# iter appelle la méthode __iter__ de mr5, qui retourne self (l'itérateur)
it = iter(mr5)

# iteration pas à pas
print(next(it)) # 0
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 4
next(it) # StopIteration

# %%

import csv

with open("data.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerow(["name", "age"])
  writer.writerow(["Alice", 30])
  writer.writerow(["Bob", 25])

with open("data.csv", "r") as f:
  # ici le reader est directement un itérateur, pas besoin d'appeler iter()
  reader = csv.reader(f)
  # une iteratin manuelle pour enlever l'entête
  header = next(reader)
  # je boucle sur les données
  for row in reader:
    print(row)


# %%
# list est un itérable, mais pas un itérateur
lst = [1, 2, 3]
it = iter(lst)
next(it)
# %%
## itérateurs spécialisés: le module itertools

from itertools import permutations, combinations, product

pool = "abcd"
p = permutations(pool, 2) # permutations de 2 éléments parmi les 4 de pool
c = combinations(pool, 2) # combinaisons de 2 éléments parmi les 4 de pool
pc = product(pool, repeat=2) # produit cartésien de pool avec lui-même
list(p)
print("="*50)
list(c)
print("="*50)
list(pc)
# %%

## brute force: trouver un secret (mot de passe) en essayant beaucoup de valeurs possibles

# module contenant des aglo de hachage utilisés pour les signatures numérique
from hashlib import md5
from string import ascii_lowercase
from time import time
import itertools

# il faut tester tous les mots (association de lettres) de longueurs 1, 2, 3, ...
# jusqu'à trouver une signature égale à celle du secret
# attention: les itérateurs génèrent beaucoup de valeurs !!!


# section principale du programme
if __name__ == "__main__":
  # mot de passe de lettres en minuscules signé par l'algo md5
  secret = "3ed7dceaf266cafef032b9d5db224717"

  ## exemple
  target = "exemple"
  # transformer la chaine de caractère UTF-8 en tableau d'octet
  octets = bytes(target, "utf-8")
  # générer la signature et on la convertit en str en hexadécimal
  hash = md5(octets).hexdigest()
  print(hash)





# %%
