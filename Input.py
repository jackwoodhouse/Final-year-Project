import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class Language:

    def __init__(self, text):

        self.Text = text

    def f1(self):

        stop_words = set(stopwords.words("english"))
        words = word_tokenize(self.Text)
        filtered_sentence = []

        for w in words:
            if w not in stop_words:
                filtered_sentence.append(w)

        return filtered_sentence


