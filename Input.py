import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import re
import csv
import pandas

# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'
# POS	possessive ending	parent\'s
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when

class Language:

    def __init__(self, text):

        self.Text = text

    def processContent(self):

        genderRegex = r"[G|g]ender:\s?[a-zA-Z]+"
        ageRegex = r"[A|a]ge:\s?[0-9]+"
        locationRegex = r"[L|l]ocation:\s?[a-zA-Z]+"

        words = self.Text

        genderMatch = re.search(genderRegex, words, re.MULTILINE)

        ageMatch = re.search(ageRegex, words, re.MULTILINE)

        locationMatch = re.search(locationRegex, words, re.MULTILINE)

        print(genderMatch.group().split()[1])
        print(ageMatch.group().split()[1])
        print(locationMatch.group().split()[1])


        # user input validatio here or on gui side


        # stop_words = set(stopwords.words("english"))
        #
        # # words = word_tokenize(self.Text)
        #
        # filtered_sentence = []
        #
        # for w in words:
        #     if w not in stop_words:
        #         filtered_sentence.append(w)

        # f = open('data.csv')
        #
        # csv_f = csv.reader(f)
        #
        # for row in csv_f:
        #     print(row)

        data = pandas.read_csv("data.csv", index_col=0)

        data.index = ["GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF",
                      "GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF",
                      "GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF"]

        print(data)


        # compare the user input to the csv files from pandas

        # return the correct csv info to the user
        return words

