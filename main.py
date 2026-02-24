"""
programme principal: qui configure un fichier de log
pour enregistrer des événements dans le programme (résultats attendus, erreurs, debug, ...)
"""

# importer c'est EXECUTER le contenu complet du module importé
# tant que le contenu du module importé ne change pas alors 
# on exécute directement le fichier .pyc dans le dossier __pycache__ (+ rapide)
# import imported_module
import sys
import logging
# import avec espace de nom => protection contre les collisions de nom
import crypto
# import sans espace de nom => plus court mais collision possible
# from crypto import brute_force
# from crypto import brute_force as bf => alias pour gérer une collision


# liste des arguments de la commande python
SEVERITY = logging.INFO if "--debug" not in sys.argv else logging.DEBUG

# configurer le fichier de log ici
# niveaux de sevérité: debug, info, warning, error, critical
# format: propriétés attendus dans le message: ici date - severité: message
logging.basicConfig(
  filename="log.txt",
  # les messages loggés doivent avoir le niveau de sévérité minimum INFO
  level=SEVERITY,
  format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s : %(message)s"
)

# collision possible
# brute_force = 2

if __name__ == "__main__":
  print(f"nom du module principal: {__name__}")
  
  logging.info("bootstrap du programme !")
  ## print(imported_module.add(2, 3)) 
  ## dir affiche tous les attributs d'une variable
  ## print(dir(imported_module))
  ## print(f"nom du module importé: {imported_module.__name__}")
  secret = "3ed7dceaf266cafef032b9d5db224717"
  
  try:
    print(crypto.brute_force(secret))
  except (ValueError, ZeroDivisionError) as e:
    print(e)
  except TypeError as e:
    print(f"spécial pour les erreurs de types: {e}")
  except Exception as e:
    print("capture tout sauf value et type")