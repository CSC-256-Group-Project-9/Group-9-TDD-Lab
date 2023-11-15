# This script is used for TDD.
# This script will test the ui class for a ContactBook
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from unittest.mock import patch
from ui import CLI
from constants_messages import UIMessages, PersonMessages, ContactBookMessages
from contactBook import ContactBook

valid_person = {
    "name": "John Doe",
    "address": "123 Main St",
    "phone_number": "1234567890",
    "email": "jDoe@example.com"
}


class TestUI(unittest.TestCase):

    def setUp(self):
        """
        Initialization of test cases
        """
        self.contact_book = ContactBook()
        self.cli = CLI(self.contact_book)

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
        # Get string representation of menu
        menu = self.cli.display_menu()

        # Test menu string against expected menu
        expected_menu = ("Menu:\n"
                         "1. Add Contact\n"
                         "2. Remove Contact\n"
                         "3. List Contacts\n"
                         "4. Exit\n")
        self.assertEqual(menu, expected_menu,
                         f'Expected {expected_menu} but got {menu}')

    def test_invalid_menu_option(self):
        """
        Input an invalid option for display menu
        and check for an appropriate error message
        """
        # Using patch, simulate user input 'h',
        # which is expected to be an invalid option, and '4' to exit.
        with patch('builtins.input', side_effect=['h', '4']):
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()
                # Assert that the invalid menu option was printed.
                mock_print.assert_any_call(UIMessages.INVALID_MENU_OPTION)

    def test_successful_add_person_prompt(self):
        """
        Test to check if correct message is displayed
        when adding a valid person to Contact Book
        """
        # Using patch, simulate user input for a valid person
        input_values = [valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"]]
        with patch('builtins.input', side_effect=input_values):
            self.cli.add_contact()

        # Verify the contact list went from empty to 1
        self.assertEqual(len(self.contact_book.contact_list), 1,
                         'Contact not added to list.')

        # Verify the contact list contains the correct information
        contact = self.contact_book.contact_list[0]
        self.assertEqual(contact.name, valid_person["name"],
                         "Name does not match.")
        self.assertEqual(contact.address, valid_person["address"],
                         "Address does not match.")
        self.assertEqual(contact.phone_number, valid_person["phone_number"],
                         "Name does not match.")
        self.assertEqual(contact.email, valid_person["email"],
                         "Name does not match.")

    def test_invalid_add_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding an invalid person to Contact Book
        """
        # User Input: '1' - Add Contact, '' - Empty String (invalid name),
        # '4' - Exit
        input_values = ['1', '', '4']
        # Using patch, simulate user input
        with patch('builtins.input', side_effect=input_values):
            # Using patch, get print from calls
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()

        # Verify expected message is in mock calls
        expected_message = PersonMessages.EMPTY_NAME
        self.assertTrue(any(expected_message in str(call) for call in mock_print.mock_calls),
                        'Empty name message not displayed.')

    def test_add_existing_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding a person to Contact Book that already exists
        """
        # Using patch, simulate user input for a valid person and a duplicate
        input_values = ['1', valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"],
                        '1', valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"], '4']
        with patch('builtins.input', side_effect=input_values):
            # Using patch, get print from calls
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()

        # Verify expected message is in mock calls
        expected_message = ContactBookMessages.DUPLICATE_CONTACT
        self.assertTrue(any(expected_message in str(call) for call in mock_print.mock_calls),
                        'Duplicate error message not displayed.')

    def test_successful_remove_contact(self):
        """
        Test to check if correct message is displayed
        when removing a valid person from Contact Book
        """
        # Using patch, simulate user input for a valid person
        input_values = [valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"]]
        with patch('builtins.input', side_effect=input_values):
            self.cli.add_contact()

        # Verify the contact list has been updated to 1 contact
        self.assertEqual(len(self.contact_book.contact_list), 1,
                         'Contact not added to list.')

        # Using patch, simulate user input for a valid person
        input_values = [valid_person["name"]]
        with patch('builtins.input', side_effect=input_values):
            self.cli.remove_contact()

        # Verify the contact list is now empty
        self.assertEqual(len(self.contact_book.contact_list), 0,
                         'Contact not removed from list.')

    def test_remove_nonexistent_contact(self):
        """
        Test to check if the appropriate error message is displayed
        when removing a contact that does not exist.
        """
        # Input values: '2' - Remove Contact, invalid person name, '4' - Exit
        input_values = ['2', 'invalid_name', '4']

        # Using patch, simulate user input
        with patch('builtins.input', side_effect=input_values):
            # Using patch, get print from calls
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()

        # Verify expected message is in mock calls
        expected_message = 'Contact invalid_name not in Contact Book.'
        self.assertTrue(any(expected_message in str(call) for call in mock_print.mock_calls),
                        'Error message not displayed.')

    def test_empty_contact_book_display(self):
        """
        Test to verify the correct message is displayed when contact book is empty
        """
        # Input Values: '3' - Display List (empty list), '4' - Exit
        input_values = ['3', '4']
        # Using patch, simulate user input
        with patch('builtins.input', side_effect=input_values):
            # Using patch, get print from calls
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()

        # Verify expected message is in mock calls
        expected_message = UIMessages.EMPTY_CONTACT_BOOK
        self.assertTrue(any(expected_message in str(call) for call in mock_print.mock_calls),
                        'Empty contact book message not displayed.')

    def test_list_contacts(self):
        """
        Add contacts to contact book and verify the contents are displayed correctly
        """
        # Input Values: '1' - Add Contact, valid person information,
        # '3' - Display List, '4' - Exit
        input_values = ['1', valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"], '3', '4']
        # Using patch, simulate user input
        with patch('builtins.input', side_effect=input_values):
            # Using patch, get print from calls
            with patch('builtins.print') as mock_print:
                self.cli.main_loop()

        # Verify expected string is in mock calls
        expected_phone = '(123)456-7890'
        expected_string = (f"Name: {valid_person['name']}, Address: {valid_person['address']},"
                           f" Phone: {expected_phone}, Email: {valid_person['email']}")
        self.assertTrue(any(expected_string in str(call) for call in mock_print.mock_calls),
                        'Incorrect contact display.')


# execute the script
if __name__ == "__main__":
    unittest.main()
