# %%

# un générateur est une "fonction" qui n'utilise pas l'instruction return
# MAIS l'instruction "yield"

def my_func():
  # return termine la fonction
  return "truc"
  return "autre truc"

# fonction génératrice
def my_gen():
  yield "truc"
  yield "autre truc"


my_func()

# l'appel à la fonction génératrice retourne un objet générateur 
g = my_gen()
# next exécute le bloc de la fonction génératrice et s'arrête au prochain "yield"
next(g)
# 2ème next l'exéctuion de génératrice recommence à partir du yield précédent 
next(g)
# 3ème next: plus de yield donc çà plante
next(g)
# %%
# générateur dans for
def my_gen():
  yield "truc"
  yield "autre truc"

for val in my_gen():
  print(val)


# %%
# FINALITE DES GENETATEURS vs LISTE

# lst = ["truc", "autre truc"]
# for val in lst:
#   print(val)
import sys

values = list(range(10000))
print(f"taille d'une liste de 10k val: {sys.getsizeof(values)}")

def my_gen_10k():
  for i in range(10000):
    # les données sont rendues à la volée, à la discrétion de l'utilisateur
    yield i

g = my_gen_10k
print(f"taille d'un générateur qui peut rendre 10k val: {sys.getsizeof(g)}")

# %%
import sys
# range est un générateur !!
r = range(100000)
print(r, sys.getsizeof(r))

# %%
