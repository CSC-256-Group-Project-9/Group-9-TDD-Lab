# This script is used for TDD.
# This script will test the PersonValidator class
# Authors: Zach Walker, David Smedberg, Owen Cawlfield

import unittest
from person_validator import PersonValidator


class TestPerson(unittest.TestCase):

    def setUp(self):
        """
        Initialization of test cases
        """
        self.validator = PersonValidator()

    def test_validate_person_name(self):
        """Test if the validator can validate a correct person name"""

    def test_validate_person_name_non_string(self):
        """Test if the validator raises an error for a non-string for name"""

    def test_validate_person_name_empty_string(self):
        """Test if the validator raises an error for an empty string for name"""

    def test_validate_person_name_too_long(self):
        """Test if the validator raises an error for a string too long for name"""

    def test_validate_person_address(self):
        """Test if the validator can validate a correct address"""

    def test_validate_person_address_non_string(self):
        """Test if the validator raises an error for a non-string for address"""

    def test_validate_person_address_empty_string(self):
        """Test if the validator raises an error for an empty string for address"""

    def test_validate_person_address_too_long(self):
        """Test if the validator raises an error for a string too long for address"""

    def test_validate_person_phone_number(self):
        """Test if the validator can validate a correct phone number"""

    def test_validate_phone_number_non_integer(self):
        """Test if the validator raises an error for a non-integer phone number"""

    def test_validate_phone_number_invalid_amount(self):
        """
        Test if the validator raises an error for when the phone number
        provided does not meet the required number of digits.
        """

    def test_validate_person_email(self):
        """Test if the validator can validate a correct email"""

    def test_validate_person_email_non_string(self):
        """Test if the validator raises an error for a non-string for email"""

    def test_validate_person_email_empty_string(self):
        """Test if the validator raises an error for an empty string for email"""

    def test_validate_person_email_too_long(self):
        """Test if the validator raises an error for a string too long for email"""


# execute the script
if __name__ == "__main__":
    unittest.main()
