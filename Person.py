
class User:

    class_counter = 1

    def __init__(self, first_name, last_name, description):

        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.unique_Id = User.class_counter
        User.class_counter += 1

    def display_user(self):
        print("ID : ", self.unique_Id, " First Name : ", self.first_name, " Last Name : ", self.last_name,
              " Your information : ", self.description)

