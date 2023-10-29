# This script is used for TDD. 
# This script will test the ContactBook class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from contactBook import ContactBook


class TestContactBook(unittest.TestCase):

    def test_ContactBook_initialization(self):
        """
        Test the initialization of a ContactBook instance.
        """

    def test_display(self):
        """
        Test the string representation of Contact list.
        """

    def test_add_contact(self):
        """
        Test to check if contact is added correctly to the ContactBook
        """

    def test_find_contact(self):
        """
        Test to check if the correct contact is returned when finding contact
        """

    def test_remove_contact(self):
        """
        Test to check if the correct contact is removed from the ContactBook
        """

    def test_remove_nonexistent_contact(self):
        """
        Test to check if the appropriate error message is raised
        when removing a contact that does not exist.
        """

    def test_empty_contact_book_display(self):
        """
        Test to verify the correct message is displayed when contact book is empty
        """


# execute the script
if __name__ == "__main__":
    unittest.main()
