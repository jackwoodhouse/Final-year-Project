import nltk
from nltk import word_tokenize


class Language:


    def __init__(self, text):

        self.Text = text


    def f1(self):

        words = nltk.word_tokenize(self.Text)
        return words
