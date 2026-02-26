# %%

import re

target = "chat shah châs"
wrong_match_target = "le petit chat est là"

# match: correspondance entre la regex à gauche et une cible qui débute avec la regex
m = re.match("chat", target)
if m:
  print("chat est au début de la 1ère cible")

m = re.match("chat", wrong_match_target)
print(m)

# search: cherche la 1ère occurence de la regex dans la cible
m = re.search("chat", wrong_match_target)
if m:
  print(f"chat est présent dans la 2ème cible: position: {m.span()}")

m = re.search("^chat", wrong_match_target)
print(m)

# %%
import re

year = "2100"
m = re.match("2(00[1-9]|0[1-9][0-9]|100)", year)
if m:
  print(f"{year} est une année du 21ème siècle")


# %%
import re
# classe de caractères: [abc], [a-z], [0-9], [a-zA-Z0-9_]: choix pour 1 caractère
## quantificateurs: *, +, ?, {n}, {n,}, {n,m}
# *: 0 ou plusieurs occurrences du motif précédent
# +: 1 ou plusieurs occurrences du motif précédent
# {n,m}: entre n et m occurrences du motif précédent

# username_regex = "^[a-zA-Z0-9_#-]*$"
# username_regex = "^[a-zA-Z0-9_#-]+$"
username_regex = "^[a-zA-Z0-9_#-]{3,20}$"

re.search(username_regex, "")
re.search(username_regex, "a")
re.search(username_regex, "mlamamra")

# %%

protcol_http_regex = "https?://"
print(re.search(protcol_http_regex, "http://example.com"))
print(re.search(protcol_http_regex, "https://example.com"))
# %%
# matthieu.lamamra@yahoo.fr
# \ : caractère d'échappement pour les caractères spéciaux
regex_email = r"[a-zA-Z0-9_+-]+(\.[a-zA-Z0-9_+-])*@[a-zA-Z0-9.-]+(\.[a-zA-Z0-9_+-])*\.[a-zA-Z]{2,}"

print(re.search(regex_email, "matthieu.lamamra@yahoo.fr"))
# %%

document_compromettant = "password: admin1234"

document_compromettant = re.sub("admin[0-9]+", "*******", document_compromettant)
print(document_compromettant)
# %%
