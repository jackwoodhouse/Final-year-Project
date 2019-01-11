
class User:

    class_counter = 0

    def __init__(self, firstName, lastName, age, location, gender):


        self.firstName = firstName
        self.lastName = lastName


        self.uniqueId = User.class_counter
        User.class_counter += 1

    def displayUser(self):
        print("ID : ", self.uniqueId, "First Name : ", self.firstName, "Last Name : ", self.lastName)

