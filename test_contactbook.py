# This script is used for TDD. 
# This script will test the ContactBook class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from contactBook import ContactBook
from unittest.mock import Mock
from constants_messages import ContactBookMessages


class TestContactBook(unittest.TestCase):

    def setUp(self):
        """Initialization of test cases"""
        # Create contact book and assign to contacts variable
        self.contacts = ContactBook()

        # Mock person 1
        self.mock_person = Mock()
        self.mock_person.name = 'Betty Carlos'
        self.mock_person.address = '123 Main St'
        self.mock_person.phone_number = '(123)456-7890'
        self.mock_person.email = 'betty@example.com'

        # Mock person 2
        self.mock_person2 = Mock()
        self.mock_person2.name = 'Joyce Greene'
        self.mock_person2.address = '456 South Main St'
        self.mock_person2.phone_number = '(987)654-3210'
        self.mock_person2.email = 'joyce@example.com'

        # Correct way to set the __str__ method for a mock object
        self.mock_person.__str__ = Mock(
            return_value="Name: Betty Carlos, Address: 123 Main St, Phone: (123)456-7890, Email: betty@example.com")
        self.mock_person2.__str__ = Mock(
            return_value="Name: Joyce Greene, Address: 456 South Main St, Phone: (987)654-3210, "
                         "Email: joyce@example.com")

    def test_ContactBook_initialization(self):
        """
        Test the initialization of a ContactBook instance.
        """
        # Using assert, verify contacts is an instance of ContactBook class
        self.assertIsInstance(self.contacts, ContactBook,
                              'ContactBook not initialized properly.')

    def test_display(self):
        """
        Test the string representation of Contact list.
        """
        # Add mock contacts to contact book
        self.contacts.add_contact(self.mock_person)
        self.contacts.add_contact(self.mock_person2)

        # Test the string representation is the same as expected string
        expected_string = (f"Name: {self.mock_person.name}, Address: {self.mock_person.address},"
                           f" Phone: {self.mock_person.phone_number}, Email: {self.mock_person.email}\n"
                           f"Name: {self.mock_person2.name}, Address: {self.mock_person2.address},"
                           f" Phone: {self.mock_person2.phone_number}, Email: {self.mock_person2.email}")
        self.assertEqual(str(self.contacts), expected_string,
                         'String representation does not match expected string.')

    def test_add_valid_contact(self):
        """
        Test to check if a valid contact is added correctly to the ContactBook
        """
        # Add contact using add_contact function
        self.contacts.add_contact(self.mock_person)

        added_person = self.contacts.contact_list[0]

        # Test to verify the person was added to the contact list.
        self.assertEqual(added_person.name, self.mock_person.name)
        self.assertEqual(added_person.address, self.mock_person.address)
        self.assertEqual(added_person.phone_number, self.mock_person.phone_number)
        self.assertEqual(added_person.email, self.mock_person.email)

    def test_add_invalid_contact(self):
        """
        Test to check if an invalid contact is not added to
        the ContactBook by using a bad name
        """
        # Create a Mock invalid person
        mock_invalid_person = Mock()
        mock_invalid_person.name = 123
        mock_invalid_person.address = "123 Main Street"
        mock_invalid_person.phone_number = '(123)456-7890'
        mock_invalid_person.email = 'my_email@example.com'

        # Test to verify that the add contact function raises an error
        with self.assertRaises(ValueError) as exc:
            self.contacts.add_contact(mock_invalid_person)

        # Verify that the correct error message is displayed
        self.assertEqual(str(exc.exception), ContactBookMessages.INVALID_ADD,
                         'Correct message was not displayed.')

    def test_duplicate_contact(self):
        """
        Test to check if a contact with the same name
        is not added to the ContactBook
        """
        # Test to verify that the add contact function raises an error
        with self.assertRaises(Exception) as exc:
            self.contacts.add_contact(self.mock_person)
            self.contacts.add_contact(self.mock_person)

        # Verify that the correct error message is displayed
        expected_message = ContactBookMessages.DUPLICATE_CONTACT
        self.assertEqual(str(exc.exception), expected_message,
                         f'Expected {expected_message} but got {str(exc.exception)}')

    def test_find_contact(self):
        """
        Test to check if the correct contact is returned when finding contact
        """
        # Add mock contacts to contact book
        self.contacts.add_contact(self.mock_person)
        self.contacts.add_contact(self.mock_person2)

        # Find valid contact within the list of two contacts
        contact = self.contacts.find_contact('Betty Carlos')

        # Verify contact is the correct contact returned
        self.assertEqual(contact.name, self.mock_person.name)
        self.assertEqual(contact.address, self.mock_person.address)
        self.assertEqual(contact.phone_number, self.mock_person.phone_number)
        self.assertEqual(contact.email, self.mock_person.email)

    def test_find_nonexistent_contact(self):
        """
        Test to check if the correct message is displayed when
        searching for a non-existing contact
        """
        # Add mock contacts to contact book
        self.contacts.add_contact(self.mock_person)
        self.contacts.add_contact(self.mock_person2)

        # Attempt to find non-existent contact within the list of two contacts
        # Verify that an Exception is raised
        name = 'John Doe'
        with self.assertRaises(Exception) as exc:
            self.contacts.find_contact(name)

        # Verify that the correct error is returned
        expected_message = f'Contact {name} not in Contact Book.'
        self.assertEqual(str(exc.exception), expected_message,
                         f'Expected {expected_message} but got {str(exc.exception)}')

    def test_remove_contact(self):
        """
        Test to check if the correct contact is removed from the ContactBook
        """
        # Add mock contacts to contact book
        self.contacts.add_contact(self.mock_person)
        self.contacts.add_contact(self.mock_person2)

        # Verify the contact book is not empty
        self.assertEqual(len(self.contacts.contact_list), 2,
                         'Contacts not added to contact list.')

        # Remove contact from list
        self.contacts.remove_contact(self.mock_person.name)

        # Verify the correct contact was removed
        # Check to see if the contact list only contains 1 person
        self.assertEqual(len(self.contacts.contact_list), 1)
        # Verify the remaining contact is correct
        contact = self.contacts.contact_list[0]
        self.assertEqual(contact.name, self.mock_person2.name,
                         'Incorrect person removed from contact list.')

    def test_remove_nonexistent_contact(self):
        """
        Test to check if the appropriate error message is raised
        when removing a contact that does not exist.
        """
        # Add mock contacts to contact book
        self.contacts.add_contact(self.mock_person)

        # Verify the contact book is not empty
        self.assertEqual(len(self.contacts.contact_list), 1,
                         'Contacts not added to contact list.')

        # Verify removing contact raises an error when attempting
        # to remove a contact that does not exist
        name = 'John Doe'
        with self.assertRaises(Exception) as exc:
            self.contacts.remove_contact(name)

        # Verify the correct error is displayed
        expected_message = f'Contact {name} not in Contact Book.'
        self.assertEqual(str(exc.exception), expected_message,
                         f'Expected {expected_message} but got {str(exc.exception)}')


# execute the script
if __name__ == "__main__":
    unittest.main()
