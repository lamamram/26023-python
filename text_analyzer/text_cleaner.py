from string import punctuation
import re

class Cleaner:
    def __init__(self, text):
        self.__text = text

    def __clean_punctuation(self):
        self.__text = re.sub(f"[{punctuation}]", " ", self.__text)

    def __clean_end_lines(self):
        self.__text = re.sub(r"\r?\n", " ", self.__text)

    def __clean_spaces(self):
        self.__text = re.sub(" +", " ", self.__text)
    
    def __clean_little_words(self):
        words = self.__text.split()
        words = list(filter(lambda word: len(word) > 3, words))
        self.__text = " ".join(words)

    def clean(self):
        self.__clean_punctuation()
        self.__clean_end_lines()
        self.__clean_spaces()
        self.__clean_little_words()
        return self.__text.lower()