class Counter:
    def __init__(self, text):
      self.__text = text

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