# %%
## forme générale des fonctions en python
def func(pos1: int, pos2: int, /, named1: list="default", *args, **kwargs) -> None:
    """ fonction 
    *args : arguments positionnels optionnels
    *args: disponibles dans le corps de la fonction dans le tuple args 
    **kwargs: arguments nommés optionnels
    **kwargs: disponibles dans le corps de la fonction dans le dictionnaire kwargs
    les annotations sont informatives (pas de contrôle de type)
    / : limite des arguments positionnels qu'on doit appeler de manière positionnelle
    entre / et *: arguments appelables de façon positionnelle ou nommée ou occultée
    après *, arguments nommés qu'on doit appeler de manière nommée (non occultable)
    """
    pass

# func est un objet de type function
# EN PYTHON TOUT EST OBJET
print(func.__annotations__)
print(func.__doc__)
# %%
## rappel sur les fonctions standard

# définition d'une fonction

# annotations de paramètres et valeur de retour
def ma_fonc(pos: str, opt: str="default", **kwds) -> tuple:
  """
  docstring: description de la fonction
  """
  return pos, opt, kwds

# l'appel
## paramètre positionnel == obligatoire => SUJET de la fonction
# ma_fonc()
ma_fonc("positionnel", "nommé")
## valeur par défaut => valeur utilisé ~90% du temps
ma_fonc("positionnel")
## paramètres "variadics" nommés => paramètres de confort, cosmétiques
ma_fonc("positionnel", truc="machin", bidule="chose")

# %%
def variance(x: float, y: float, order: int=2, **opts) -> float:
  """
  fonction statistique: racine nième de la somme de deux nombre à la puissance de n
  
  mode DEBUG avec le paramètre debug à True
  """
  if "debug" in opts and opts["debug"]:
    print(f"DEBUG: {x, y, order}")
  ret = ( x**order + y**order)**1/order
  return ret


std = variance(3, 10, debug=True)**0.5
print(f"écart type de (3, 10): {std}")
# %%
# notion de fonctions lambda
## fonctions qui utilisent des fonctions

numbers = [1, 2, 3, 4, 5]

def square(x: float) -> float:
  return x**2

## façon programmation impérative/procédurale
# squares = []
# for nb in numbers:
#   squares.append(square(nb))
# print(squares)

def my_map(f: "function", objs: list) -> list:
  transformed = []
  for obj in objs:
    transformed.append(f(obj))
  return transformed

## façon programmation fonctionnelle
## y = f ° g(x) = f(g(x))
print(my_map(square, numbers))


# %%
# fonctions lambdas: fonctions sans nom, à usage unique

numbers = [1, 2, 3, 4, 5]
def my_map(f: "function", objs: list) -> list:
  transformed = []
  for obj in objs:
    transformed.append(f(obj))
  return transformed

print(my_map(lambda x: x**2, numbers))

# %%
# usages principaux: le map => appliquer à chaque élément d'un itérable, une fonction

numbers = list(range(1000))
## map est une primitive programmée en C => bcp plus rapide que la boucle for
list(map(lambda x: x**2, numbers))
# %%

# usages principaux: le filtrage: conserver les éléments d'un itérable 
# qui retournent True à une fonction en paramètre
numbers = list(range(1000))
# n%5 = reste de n divisé par 5 : 0 => multiple de 5
list(filter(lambda n: n%5 == 0, numbers))
# %%
import random
# usage principaux: le tri

# liste en intension
rows = [ f"row_{i}" for i in range(1, 21) ]
random.shuffle(rows)
rows

# trier la liste rows dans l'ordre décroissant 
# des entiers à la fin de chaque chaine de caractère
sorted(rows, key=lambda "???")


# %%
