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
# fermeture
conn.close()
# %%
# idem avec un gestionnaire de contexte

with sqlite3.connect("dns.db") as conn:
  cur = conn.cursor()
  query = "SELECT SQLITE_VERSION()"
  cur.execute(query)
  row = cur.fetchone()
  print(row)

# le close() est automatique

# %%
