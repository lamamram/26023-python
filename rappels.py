# module standard: pas besoin d'utiliser pip
import json
# module tiers: installé à partir de pip, dans l'environnement virtuel
import requests

user_data = {
  "name": "John Doe",
  "age": 30,
  "email": "john@example.com"
}

# sérialiaser en json
# json_string = json.dumps(user_data)
# print(json_string, type(json_string))

response = requests.get("https://www.dawan.fr/")

print(f"""
      code de réponse de l'url : {response.status_code}
      url fonctionnelle ? { 200 <= response.status_code < 300 }
""")

# contenu de type 'page html' donc texte
if "text/html" in response.headers["Content-Type"]:
  print(response.text)
