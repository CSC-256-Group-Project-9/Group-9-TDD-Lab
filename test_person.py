# This script is used for TDD.
# This script will test the Person class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from person import Person


class TestPerson(unittest.TestCase):

    def test_person_initialization(self):
        """
        Test the initialization of a Person instance.
        """

    def test_person_display(self):
        """
        Test the string representation of a Person
        """

    def test_person_name_setter(self):
        """
        Test the setter for changing the person's name
        """

    def test_person_address_setter(self):
        """
        Test the setter for changing the person's address
        """

    def test_person_phone_number_setter(self):
        """
        Test the setter for changing the person's phone number
        """

    def test_person_email_setter(self):
        """
        Test the setter for changing the person's email
        """


# execute the script
if __name__ == "__main__":
    unittest.main()

