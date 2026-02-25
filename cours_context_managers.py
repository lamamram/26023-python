# %%

# client de connexion avec une base de donnée sqlite3 avec un gestionnaire de contexte

import sqlite3

## avec toutes les base données en python on peut utiliser les 7 méthodes usuelles
## connect() => connexion à la base
## cursor() => se donner un prompt sur la connexion
## execute(query) => exécuter une ou plusieurs requêtes SQL dans le curseur
## fetch() => rapatrier les données de la réponse de la requête
## gestion de transaction
## commit() => confirmer que les requêtes se sont bien exécutées
## rollback() => infirmer les requêtes précédentes s'il ya un pb
## close() => fermer la connexion

# ouverture
conn = sqlite3.connect("dns.db")
cur = conn.cursor()
# requête SQL: retourne un enregistrement avec une seule colonne
query = "SELECT SQLITE_VERSION()"
cur.execute(query)
row = cur.fetchone()
print(row)
# fermeture: pour éviter les fuites de mémoire (memory leaks)
conn.close()
# %%
# idem avec un gestionnaire de contexte

with sqlite3.connect("dns.db") as conn:
  cur = conn.cursor()
  query = "SELECT SQLITE_VERSION()"
  # exécute une SEULE REQUETE SQL
  cur.execute(query)
  row = cur.fetchone()
  print(row)

# le close() est automatique

# %%
## générer les tables et insérer les données à partir d'un script
with sqlite3.connect("dns.db") as conn:
  cur = conn.cursor()
  with open("domain_names_sqlite3.sql", "r", encoding="utf-8") as f:
    # lire le contenu du fichier dans une variable
    script = f.read()
  # exécute un ensemble de requêtes
  cur.executescript(script)
  # nb d'éléments modifiés (crées/modifiés/supprimés)
  print(f"nb d'éléments insérés: {cur.rowcount}")

