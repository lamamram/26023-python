# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

# %%

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": "500",
    "section": "30",
    "debit": "2"
}

# %%
start_index = _template.index("((") + len("((")
end_index = _template.index("))")
key = _template[start_index:end_index]

# ----------------      OLD        ,       NEW
_template.replace("((" + key + "))", injections[key])

# %%

while "((" in _template:
  start_index = _template.index("((") + len("((")
  end_index = _template.index("))")
  key = _template[start_index:end_index]
  _template = _template.replace("((" + key + "))", injections.get(key, "N/A"))

print(_template)


# %%

def parse_template(
        tpl: str, 
        values: dict, 
        delim: tuple=("{{","}}"), 
        default: str="N/A",
        **opts
) -> str:
    """
    fonction d'interprétation d'un fichier template pour injecter
    des valeurs venues d'un diction
    **opts: "debug", "log", ...
    """
    # plus optimisé
    while '((' in tpl:
    # while tpl.count(delim[0]):
        start_index = tpl.index(delim[0])
        end_index = tpl.index(delim[1])
        key = tpl[start_index + len(delim[0]):end_index]
        if "debug" in opts and opts["debug"]:
            print(f"key: {key}")
        val = values.get(key, default)

        tpl = tpl.replace(delim[0] + key + delim[1], str(val))
    return tpl

# %%

print(parse_template(_template, injections, ("((","))"), "N/A"))

# %%
