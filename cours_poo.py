# %%

account = {
  "id": 13123431,
  "balance": 100.,
  "overdraft": 100.
}

def withdraw(acc: dict, amount: float) -> None:
  if acc["balance"] + acc["overdraft"] > amount:
    acc["balance"] -= amount
  else:
    raise ValueError(f"montant interdit: {amount}")

withdraw(account, 100)
withdraw(account, 200)

print(account["balance"])
  


# %%
## idem en POO: on créé un type de donnée custom sur un domaine
## professionnel qui rassemble les données internes (attributs) et
## les fonctions intéragissant sur ces données (méthodes)

class Account:
  
  # attribut de classe (de données spécifiques à la classe)
  id = 0
  balance = 0.
  overdraft = 0.

  def withdraw(self, amount: float) -> None:
    if self.balance + self.overdraft > amount:
      self.balance -= amount
    else:
      raise ValueError(f"montant interdit: {amount}")


# instanciation de l'objet à partir de la classe
acc = Account()
# valeur des attributs de l'objet
acc.id = 13123431
acc.balance = 100.
acc.overdraft = 100.

# les attributs de classe ne sont pas liés aux attributs de l'objet
print(Account.balance)

acc.withdraw(100)
# acc.withdraw(200)
# %%

## la méthode magique __init__ permet d'alimenter l'objet au moment de l'instanciation

class Account:

  def __init__(self, id: int, balance: float, overdraft: float=100.) -> None:
    self.id = id
    self.balance = balance
    self.overdraft = overdraft

  def withdraw(self, amount: float) -> None:
    if self.balance + self.overdraft > amount:
      self.balance -= amount
    else:
      raise ValueError(f"montant interdit: {amount}")

# ----------- effet de __init__
acc = Account(1234243, 100.)
acc.withdraw(100)

# je peux afficher la valeur de l'attribut balance depuis l'extérieur de la classe
# balance est public
print(acc.balance)

# on peut également mettre à jour directement le solde à partir de l'objet
acc.balance += 100
print(acc.balance)

# %%

## encapsulation: attributs/méthodes publics ou privés

class Account:

  def __init__(self, id: int, balance: float, overdraft: float=100.) -> None:
    ## un attribut préfixé par "__" devient PRIVE
    self.__id = id
    self.__balance = balance
    self.__overdraft = overdraft

  ### METHODES PUBLIQUES: sont les seuls accès possible 
  # pour interagir avec les attributs privés
  # utiles pour contôler les données d'entrées / sortie 
  # les méthodes exploitent les règles et données critiques de l'entreprise

  def deposit(self, amount: float) -> None:
    if amount > 0:
      self.__set_balance(amount)
    else:
      raise ValueError(f"montant négatif {amount} !!!")  

  def withdraw(self, amount: float) -> None:
    if amount <= 0:
      raise ValueError(f"montant négatif ou nul {amount} !!!")
    if self.__balance + self.__overdraft > amount:
      self.__set_balance(-amount)
    else:
      raise ValueError(f"montant interdit: {amount}")
  
  ## getter: une méthode qui retourne un attribut privé
  def get_balance(self):
    # ici on peut contrôler ce que on veut afficher
    return self.__balance
  
  ### METHODE PRIVEE: responsable de la modification de l'état de l'objet 
  # état == ensemble des valeurs des attributs
  def __set_balance(self, amount):
    self.__balance += amount

if __name__ == "__main__":

  acc = Account(13345, 100.)

  acc.withdraw(100)

  ## PRIVE = on ne peut pas afficher / mettre à jour l'attribut à partir de l'extérieur de la classe
  # print(acc.__balance) => AttributeError

  print(acc.get_balance())
# %%

"""
Règles de bases de la Programmation Orientée Objet
1/ on ne créé que des attributs privés dans le __init__
2/ ce sont les méthodes publiques qui permettent d'intéragir entre le contexte extérieur (prog. principal)
2b/ les méthodes publiques implémentent les contrôles liés aux règles du métier
3/ les méthodes privées ont la responsabilité de mettre à jour l'état des objets


Prog. principal
|
on importe la classe depuis un module
on instancie un objet à partir de la classe et on lui donne des valeurs
----- objet
      |
      on exécute des méthodes publiques pour intéragir avec les attributs
      ces méthodes font du contrôle (try/except | if ...)
      ----- méthode publique
            |
            quand les contrôle sont OK => on exécute les méthodes privées qui change l'état
            ---- méthode privée
                 |
                 modifient les attributs privés
                                              |
                  <---------------------------
            <-----
      <-----
<-----                                  

"""
