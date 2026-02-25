# %%
"""
1/ saisir n valeurs entiers relatifs dans le clavier séparés par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
que ces valeurs sont des entiers relatifs
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

liste = input("saisissez des entiers relatifs séparés par ,")

liste = liste.split(",") 

int_list = []
for elem in liste:
  if elem.isnumeric():
    int_list.append(int(elem))
  else:
    print("erreur")

print(int_list)