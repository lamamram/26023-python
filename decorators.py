# %%
# exemple graphique

# un décorateur est une fonction qui remplacer une fonction
# par une autre qui modifie le coportement de le première

def strong(f: "function"):
  # remplacer la fonction f par une fonction qui
  # 1/ exécute f
  # 2/ ajoute un comportement supplémentatire (décoration)
  # signature universelle: prend n'importe quels paramètres
  def wrapper(*args, **kwargs):
    return "<strong>" + f(*args, **kwargs) + "</strong>"
  
  return wrapper


# une fonction qui a sa propre finalité 
@strong
def to_upper(message: str) -> str:
  return message.upper()

@strong
def to_join(words: list[str]) -> str:
  return " ".join(words)

# @ est la même chose que => remplacement
# to_upper = strong(to_upper)

## factorisation du strong dans une famille de fonction

to_upper("bonjour tout le monde")

to_join(["salut", "les", "gens"])

# avec cette technique je fois utiliser strong à chaque fois

# def strong(message: str):
#   return "<strong>" + message + "</strong>"

# strong(to_upper("bonjour tout le monde"))

# %%
# accumuler des décorateurs

def strong(f: "function"):
  def wrapper(*args, **kwargs):
    return "<strong>" + f(*args, **kwargs) + "</strong>"  
  return wrapper

def italic(f: "function"):
  def wrapper(*args, **kwargs):
    return "<em>" + f(*args, **kwargs) + "</em>" 
  return wrapper

@strong
@italic
def to_upper(message: str) -> str:
  return message.upper()

# idem à to_upper = strong(italic(to_upper))

to_upper("bonjour tout le monde")
# %%

# décorateur paramétré

def html_tags(*tags):
  def deco(f: "function"):
    def wrapper(*args, **kwargs):
      ret = f(*args, **kwargs)
      for tag in tags:
        ret = "<" + tag + ">" + ret + '</' + tag + '>'
      return ret
    return wrapper
  return deco

@html_tags("strong", "em", "u")
def to_upper(message: str) -> str:
  return message.upper()

# idem à to_upper = html_tags("strong")(to_upper)

to_upper("bonjour tout le monde")
# %%
