# This script is used for TDD. 
# This script will test the ContactBook class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from contactBook import ContactBook
from constants_messages import ContactBookMessages


class TestContactBook(unittest.TestCase):

    def test_ContactBook_initialization(self):
        """
        Test the initialization of a ContactBook instance.
        """
        # Create contact book and assign to contacts variable
        contacts = ContactBook()

        # Using assert, verify contacts is an instance of ContactBook class
        assert isinstance(contacts, ContactBook)

    def test_display(self):
        """
        Test the string representation of Contact list.
        """

    def test_add_valid_contact(self):
        """
        Test to check if a valid contact is added correctly to the ContactBook
        """

    def test_add_invalid_contact(self):
        """
        Test to check if an invalid contact is not added to the ContactBook
        """

    def test_duplicate_contact(self):
        """
        Test to check if a contact with the same name
        is not added to the ContactBook
        """

    def test_find_contact(self):
        """
        Test to check if the correct contact is returned when finding contact
        """

    def test_find_nonexistent_contact(self):
        """
        Test to check if the None is returned when
        searching for a non-existing contact
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
