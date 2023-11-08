class Person(object):

    # Deafault Constructor
    #Person has:
    # Name, Address, Phone Number, and email
    def __init__(self, name, address, phone_number, email):
        self.name = name;
        self.address = address;
        self.phone_number = phone_number;
        self.email = email;

    #Getters using decorator
    @property
    def name(self):
        return self.name
    @property
    def address(self):
        return self.address
    @property
    def phoneNum(self):
        return self.phone_number
    @property
    def email(self):
        return self.email
    
    #Setters using decorator
    @name.setter
    def name(self, value):
        self.name = value

    @address.setter
    def address(self, value):
        if (len(value) < 13): # make sure lenght is enough
            print(f"{value} is not a valid phone number")
        # add format check
        # add digit check
        else:
            self.address = value

    @phoneNum.setter
    def phoneNum(self, value):
        self.phone_number = value

    @email.setter
    def email(self, value):
        self.email = value

 #Main function for testing (well the test before running the Test script)   
def main():
    #Basic test - ensure basic sets work, pre adding conditions (phone# needs x amount of nums)
    ant = Person
    ant.name = "Anthony"
    print(ant.name)
    ant.address = "123 I Live Here Lane"
    print(ant.address)
    ant.phoneNum = "123-456-8910"
    print(ant.phoneNum)



if __name__ == "__main__":
    main()