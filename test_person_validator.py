# This script is used for TDD.
# This script will test the PersonValidator class
# Authors: David Smedberg

import unittest
from person_validator import PersonValidator
import constants_messages
from constants_messages import PersonMessages


class TestPersonValidator(unittest.TestCase):

    def setUp(self):
        """
        Initialization of test cases
        """
        self.validator = PersonValidator()

    def test_validate_person_name(self):
        """Test if the validator can validate a correct person name"""
        self.assertEqual(self.validator.validate_person_name("abc"), "abc")

    def test_validate_person_name_non_string(self):
        """Test if the validator raises an error for a non-string for name"""
        with self.assertRaises(TypeError) as e:
            self.validator.validate_person_name(12)
        self.assertEqual(str(e.exception), PersonMessages.INVALID_STRING, "Person-Non-String: Assertion Failed!")

    def test_validate_person_name_empty_string(self):
        """Test if the validator raises an error for an empty string for name"""
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_name('')
        self.assertEqual(str(e.exception), PersonMessages.EMPTY_NAME, "Person-Name-Empty: Assertion Failed!")

    def test_validate_person_name_too_long(self):
        """Test if the validator raises an error for a string too long for name"""
        long_name = "a" * (constants_messages.MAX_PERSON_NAME_LENGTH + 1)
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_name(long_name)
        self.assertEqual(str(e.exception), PersonMessages.NAME_TOO_LONG, "Person-Name-Too-Long: Assertion Failed!")


    def test_validate_person_address(self):
        """Test if the validator can validate a correct address"""
        self.assertEqual(self.validator.validate_person_address("abc"), "abc")

    def test_validate_person_address_non_string(self):
        """Test if the validator raises an error for a non-string for address"""
        with self.assertRaises(TypeError) as e:
            self.validator.validate_person_address(12)
        self.assertEqual(str(e.exception), PersonMessages.INVALID_ADDRESS_TYPE, "Address-Non-String: Assertion Failed!")

    def test_validate_person_address_empty_string(self):
        """Test if the validator raises an error for an empty string for address"""
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_address('')
        self.assertEqual(str(e.exception), PersonMessages.EMPTY_ADDRESS, "Address-Empty: Assertion Failed!")

    def test_validate_person_address_too_long(self):
        """Test if the validator raises an error for a string too long for address"""
        long_address = "a" * (constants_messages.MAX_ADDRESS_LENGTH + 1)
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_address(long_address)
        self.assertEqual(str(e.exception), PersonMessages.ADDRESS_TOO_LONG, "Address-Too-Long: Assertion Failed!")


    def test_validate_person_phone_number(self):
        """Test if the validator can validate a correct phone number"""
        self.assertEqual(self.validator.validate_person_phone_number("1234567890"), "1234567890")

    def test_validate_phone_number_non_integer(self):
        """Test if the validator raises an error for a non-integer phone number"""
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_phone_number("hamburger")
        self.assertEqual(str(e.exception), PersonMessages.INVALID_PHONE_NUMBER_TYPE, "Phone-Number-Non-Integer: Assertion Failed!")

    def test_validate_phone_number_invalid_amount(self):
        """
        Test if the validator raises an error for when the phone number
        provided does not meet the required number of digits.
        """
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_phone_number("123456")
        self.assertEqual(str(e.exception), PersonMessages.PHONE_NUMBER_WRONG_LENGTH, "Phone-Number-Invalid-Length: Assertion Failed!")


    def test_validate_person_email(self):
        """Test if the validator can validate a correct email"""
        self.assertEqual(self.validator.validate_person_email("abc@gmail.com"), "abc@gmail.com")

    def test_validate_person_email_non_string(self):
        """Test if the validator raises an error for a non-string for email"""
        with self.assertRaises(TypeError) as e:
            self.validator.validate_person_email(12)
        self.assertEqual(str(e.exception), PersonMessages.INVALID_EMAIL, "Email-Non-String: Assertion Failed!")

    def test_validate_person_email_empty_string(self):
        """Test if the validator raises an error for an empty string for email"""
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_email('')
        self.assertEqual(str(e.exception), PersonMessages.EMPTY_EMAIL, "Email-Empty: Assertion Failed!")

    def test_validate_person_email_too_long(self):
        """Test if the validator raises an error for a string too long for email"""
        long_email = "a" * (constants_messages.MAX_EMAIL_LENGTH + 1)
        with self.assertRaises(ValueError) as e:
            self.validator.validate_person_email(long_email)
        self.assertEqual(str(e.exception), PersonMessages.EMAIL_TOO_LONG, "Email-Too-Long: Assertion Failed!")


    def tearDown(self):
        self.validator.dispose()

# execute the script
if __name__ == "__main__":
    unittest.main()
    
