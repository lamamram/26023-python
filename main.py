"""
programme principal: qui configure un fichier de log
pour enregistrer des événements dans le programme (résultats attendus, erreurs, debug, ...)
"""

# importer c'est EXECUTER le contenu complet du module importé
# tant que le contenu du module importé ne change pas alors 
# on exécute directement le fichier .pyc dans le dossier __pycache__ (+ rapide)
# import imported_module

import logging
# import avec espace de nom => protection contre les collisions de nom
import crypto
# import sans espace de nom => plus court mais collision possible
# from crypto import brute_force
# from crypto import brute_force as bf => alias pour gérer une collision

# configurer le fichier de log ici
# niveaux de sevérité: debug, info, warning, error, critical
# format
logging.basicConfig(
  filename="log.txt",
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s : %(message)s"
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

  print(crypto.brute_force(secret))