import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import re
import pandas
import numpy

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

        userInput = self.Text

        genderRegex = r"[G|g]ender:\s?[a-zA-Z]+"
        ageRegex = r"[A|a]ge:\s?[0-9]+"
        locationRegex = r"[L|l]ocation:\s?[a-zA-Z]+"

        genderMatch = re.search(genderRegex, userInput, re.MULTILINE)
        ageMatch = re.search(ageRegex, userInput, re.MULTILINE)
        locationMatch = re.search(locationRegex, userInput, re.MULTILINE)

        Location = locationMatch.group().split()[1]
        Age = ageMatch.group().split()[1]
        Gender = genderMatch.group().split()[1]

        if Age >= '24':
            Age = 'All ages'
        elif Age <= '17':
         Age = '18'

        if Gender == 'Male' or Gender == 'male':
            Gender = 'Persons'
        elif Gender == 'Female' or Gender == 'female':
            Gender = 'Persons'

        print(Location)
        print(Age)
        print(Gender)

        # location: Sheffield, age: 1, gender: male

        data = pandas.read_csv("data.csv", delimiter=',',index_col=0)

        # data.index = ["GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF",
        #               "GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF",
        #               "GB", "LDR", "NOT", "YRK", "DON", "SHF", "LDS", "WKF"]

        AreaFilter = data['Area_Name'] == Location
        ageFilter = data['Age'] == Age
        genderFilter = data['Sex'] == Gender
        filter = AreaFilter & ageFilter & genderFilter

        print(data[filter])

        data[filter].to_json('results.txt')


        return userInput

