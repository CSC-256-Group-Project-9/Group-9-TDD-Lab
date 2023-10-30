# constants_messages.py
# Constance and messages related to products are maintained in this file.

# Maximum allowable lengths for Name and phone_number
MAX_PERSON_NAME_LENGTH: int = 40
PHONE_NUMBER_LENGTH: int = 13
MAX_ADDRESS_LENGTH: int = 100
MAX_EMAIL_LENGTH: int = 100
# This class respects the SRP principle by centralizing error messages


class PersonMessages:
    """
    This class provides centralized messages related to persons

    Static methods provide messages that need to incorporate dynamic values
    """

    # Error Messages/Person Name
    INVALID_STRING: str = "ERROR: Name should be a string."
    EMPTY_NAME: str = "ERROR: Name cannot be empty or contain just whitespace."
    NAME_TOO_LONG: str = f"ERROR: Name cannot be more than {MAX_PERSON_NAME_LENGTH} characters."

    # Error Messages / Address
    INVALID_ADDRESS_TYPE: str = "ERROR: Address should be a string."
    EMPTY_ADDRESS: str = "ERROR: Address cannot be empty or contain just whitespace."
    ADDRESS_TOO_LONG: str = f"ERROR: Address cannot be more than {MAX_ADDRESS_LENGTH} characters."

    # Error Messages / phone_number
    INVALID_PHONE_NUMBER_TYPE: str = "ERROR: Phone number should be a string."
    PHONE_NUMBER_WRONG_LENGTH: str = f"ERROR: Phone number should be {PHONE_NUMBER_LENGTH} characters."
    EMPTY_PHONE_NUMBER: str = "Phone number cannot be empty or contain just whitespace."

    # Error Message / Email
    INVALID_EMAIL: str = "ERROR: Email must be a valid email address format."
    EMPTY_EMAIL: str = "ERROR: Email cannot be empty or contain just whitespace."

