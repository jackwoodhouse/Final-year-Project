
class User:

    class_counter = 1

    def __init__(self, firstName, lastName, description):


        self.firstName = firstName
        self.lastName = lastName
        self.description = description
        self.uniqueId = User.class_counter
        User.class_counter += 1

    def displayUser(self):
        print("ID : ", self.uniqueId, " First Name : ", self.firstName, " Last Name : ", self.lastName, " Your information : ", self.description)

