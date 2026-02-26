# en cas de couplage fort
from text_analyzer.text_cleaner import Cleaner

class Counter:
    ## pas de couplage
    # def __init__(self, text):
      # self.__text = text
    
    ## couplage fort
    # def __init__(self, text, min_length=3):
      # self.__text = Cleaner(text, min_length).clean()
    
    ## couplage faible
    def __init__(self, cleaner: Cleaner):
      self.__text = cleaner.clean()


    def count(self):
      occurences = {}
      words = self.__text.split()
      for word in words:
        # s'il existe j'incrémente le nombre d'occurences
        if word in occurences:
          occurences[word] += 1
        # sinon je créé avec l'occurence à 1
        else:
          occurences[word] = 1
      
      return dict(sorted(
        occurences.items(), 
        key=lambda tup: tup[1], 
        reverse=True)[:5]
      )