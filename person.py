MAX_PERSON_NAME_LENGTH: int = 40
PHONE_NUMBER_LENGTH: int = 10
MAX_ADDRESS_LENGTH: int = 100
MAX_EMAIL_LENGTH: int = 100


class Person(object):

    # Default Constructor
    # Person has:
    # Name, Address, Phone Number, and email
    def __init__(self, name="", address="", phone_number="", email=""):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return "Name:" + self.name + ", Address:" + self.address + ", Phone: " + self.phone_number + ", Email: " + self.email

    # Getters using decorator

    def name(self):
        return self.name

    def address(self):
        return self.address

    def phone_number(self):
        return self.phone_number

    def email(self):
        return self.email

    # Setters using decorator
    def name(self, value):
        self.name = value

    def address(self, value):
        self.address = value

    def phone_number(self, value):
        self.phone_number = value

    def email(self, value):
        self.email = value


# Main function for testing (well the test before running the Test script)
def main():
    # Basic test - ensure basic sets work, pre adding conditions (phone# needs x amount of nums)
    ant = Person()
    ant.name = "Anthony"
    print(ant.name)
    ant.address = "123 I Live Here Lane"
    print(ant.address)
    ant.phone_number = "1234567890"
    print(ant.phone_number)

    print(ant)


if __name__ == "__main__":
    main()
