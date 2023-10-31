# This script is used for TDD.
# This script will test the ui class for a ContactBook
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from ui import CLI
from constants_messages import UIMessages


class TestUI(unittest.TestCase):

    def setUp(self):
        """
        Initialization of test cases
        """
        self.cli = CLI()

    def test_CLI_initialization(self):
        """
        Test the initialization of a CLI instance.
        """
        # Using assert, verify contacts is an instance of CLI class
        self.assertIsInstance(self.cli, CLI,
                              'CLI is not initialized properly.')

    def test_display_menu(self):
        """
        Test the string representation of the display menu.
        """

    def test_invalid_menu_option(self):
        """
        Input an invalid option for display menu
        and check for an appropriate error message
        """

    def test_successful_add_person_prompt(self):
        """
        Test to check if correct message is displayed
        when adding a valid person to Contact Book
        """

    def test_invalid_add_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding an invalid person to Contact Book
        """

    def test_add_existing_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding a person to Contact Book that already exists
        """

    def test_successful_remove_contact(self):
        """
        Test to check if correct message is displayed
        when removing a valid person from Contact Book
        """

    def test_remove_nonexistent_contact(self):
        """
        Test to check if the appropriate error message is displayed
        when removing a contact that does not exist.
        """

    def test_empty_contact_book_display(self):
        """
        Test to verify the correct message is displayed when contact book is empty
        """
        display_str = self.cli.display_list()
        self.assertEqual(display_str, UIMessages.EMPTY_CONTACT_BOOK,
                         f'Expected {UIMessages.EMPTY_CONTACT_BOOK} but got {display_str}')

    def test_list_contacts(self):
        """
        Add contacts to contact book and verify the contents are displayed correctly
        """


# execute the script
if __name__ == "__main__":
    unittest.main()
