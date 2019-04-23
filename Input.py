import re
import pandas
import numpy


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

        Location = Location.title()

        if Age <= '24':
            Age = '18-24'

        elif Age <= '50':
            Age = '25-50'

        elif Age <= '75':
            Age = '51-75'

        if Gender == 'Male' or Gender == 'male':
            Gender = 'Persons'
        elif Gender == 'Female' or Gender == 'female':
            Gender = 'Persons'


        data = pandas.read_csv("HealthData.csv", delimiter=',', index_col=0)

        AreaFilter = data['Area_Name'] == Location
        ageFilter = data['Age'] == Age
        genderFilter = data['Sex'] == Gender
        filter = AreaFilter & ageFilter & genderFilter

        print(data[filter])

        open('results.txt', 'w').close()

        data[filter].to_csv(r'results.txt', header=None, index=None, sep=' ', mode='a')
