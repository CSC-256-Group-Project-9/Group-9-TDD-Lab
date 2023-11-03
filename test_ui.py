# This script is used for TDD.
# This script will test the ui class for a ContactBook
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from unittest.mock import patch, MagicMock
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
        with patch('builtins.input', side_effect=['5', '4']):
            # Create a MagicMock to capture the output
            captured_output = MagicMock()

            with patch('sys.stdout', new=captured_output):
                self.cli.main_loop()

            # Check if the error message is displayed in the captured output
            self.assertIn(UIMessages.INVALID_MENU_OPTION, captured_output.return_value)

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
        expected_phone = "(123)456-7890"
        self.assertEqual(contact.name, valid_person["name"],
                         "Name does not match.")
        self.assertEqual(contact.address, valid_person["address"],
                         "Address does not match.")
        self.assertEqual(contact.phone_number, expected_phone,
                         "Name does not match.")
        self.assertEqual(contact.email, valid_person["email"],
                         "Name does not match.")

    def test_invalid_add_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding an invalid person to Contact Book
        """
        # Using patch, simulate user input for an invalid person name
        with patch('builtins.input', side_effect=[123]):
            # Create a MagicMock to capture the output
            captured_output = MagicMock()

            with patch('sys.stdout', new=captured_output):
                self.cli.add_contact()

            # Check if the error message is displayed in the captured output
            self.assertIn(PersonMessages.INVALID_STRING, captured_output.return_value)

        # Verify the contact list remains empty
        self.assertEqual(len(self.contact_book.contact_list), 0,
                         'Contact not added to list.')

    def test_add_existing_person_prompt(self):
        """
        Test to check if correct error message is displayed
        when adding a person to Contact Book that already exists
        """
        # Using patch, simulate user input for a valid person and a duplicate
        input_values = [valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"],
                        valid_person["name"]]
        with patch('builtins.input', side_effect=input_values):
            # Create a MagicMock to capture the output
            captured_output = MagicMock()

            with patch('sys.stdout', new=captured_output):
                self.cli.add_contact()
                self.cli.add_contact()

            # Check if the error message is displayed in the captured output
            self.assertIn(ContactBookMessages.DUPLICATE_CONTACT, captured_output.return_value)

        # Verify the contact list has only 1 contact
        self.assertEqual(len(self.contact_book.contact_list), 1,
                         'Duplicate added to list.')

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
        # Using patch, simulate user input for a valid person
        input_values = [valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"]]
        with patch('builtins.input', side_effect=input_values):
            self.cli.add_contact()

        # Verify the contact list has been updated to 1 contact
        self.assertEqual(len(self.contact_book.contact_list), 1,
                         'Contact not added to list.')

        # Using patch, simulate user input for a valid person
        name = "invalid_name"
        with patch('builtins.input', side_effect=[name]):
            # Create a MagicMock to capture the output
            captured_output = MagicMock()

            with patch('sys.stdout', new=captured_output):
                self.cli.remove_contact()

        # Verify that the correct error is returned
        expected_message = f'Contact {name} not in Contact Book.'
        self.assertEqual(captured_output.return_value, expected_message,
                         f'Expected {expected_message} but got {captured_output.return_value}')

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
        # Using patch, simulate user input for a valid person
        input_values = [valid_person["name"], valid_person["address"],
                        valid_person["phone_number"], valid_person["email"]]
        with patch('builtins.input', side_effect=input_values):
            self.cli.add_contact()

        contact_display = self.cli.display_list()
        expected_phone = '(123)456-7890'
        expected_string = (f"Name: {valid_person['name']}, Address: {valid_person['address']},"
                           f" Phone: {expected_phone}, Email: {valid_person['email']}\n")
        self.assertEqual(contact_display, expected_string,
                         f'String does not match: expected {expected_string}, but got {contact_display}')


# execute the script
if __name__ == "__main__":
    unittest.main()
