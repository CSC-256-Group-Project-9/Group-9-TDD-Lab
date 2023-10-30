# This script is used for TDD.
# This script will test the Person class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        # create a person object for each test
        self.personObject = Person("Test Person",
                                   "123 Somewhere Drive Anytown, USA",
                                   "(123)456-7890",
                                   "somewhere@someplace.com")

    def test_person_initialization(self) -> None:
        """
        Test the initialization of a Person instance.
        """
        # error message in case if test case got failed
        self.message = "given object is not instance of Person"
        # assertIsInstance() to check if objects is instance of class
        self.assertIsInstance(personObject, Person, message)

    def test_person_display(self) -> None:
        """
        Test the string representation of a Person
        """
        self.message = "Test Person's address: 123 Somewhere Drive Anytown, USA, phone number: " \
                       "1234567890, email: somewhere@someplace.com"
        self.assertEqual(self.message, str(self.personObject), msg=None)

    def test_person_name_setter(self) -> None:
        """
        Test the setter for changing the person's name
        """
        # change the person's name
        self.personObject.name = "Updated Name"

        # verify the name was changed correctly
        self.assertEqual(self.personObject.name, "Updated Name", 'name not changed correctly')

    def test_person_address_setter(self) -> None:
        """
        Test the setter for changing the person's address
        """
        # change the person's address
        self.personObject.address = "321 Updated St. Somewhere Else, USA"

        # verify the name was changed correctly
        self.assertEqual(personObject.address, "321 Updated St. Somewhere Else, USA", 'address not changed correctly')

    def test_person_phone_number_setter(self) -> None:
        """
        Test the setter for changing the person's phone number
        """
        # change the person's phone_number
        self.personObject.phone_number = "(123)456-0987"

        # verify the phone_number was changed correctly
        self.assertEqual(self.personObject.phone_number, "(123)456-0987", 'phone_number not changed correctly')

    def test_person_email_setter(self) -> None:
        """
        Test the setter for changing the person's email
        """
        # change the person's email
        self.personObject.email = "differentemail@someplace.com"

        # verify the email was changed correctly
        self.assertEqual(self.personObject.email, "differentemail@someplace.com", 'email not changed correctly')

    # dispose of each object after each test
    def tearDown(self):
        self.personObject.dispose()


# execute the script
if __name__ == "__main__":
    unittest.main()

