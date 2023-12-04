import constants_messages
from constants_messages import PersonMessages

class PersonValidator:
    def __init__(self):
        pass

    def validate_person_name(self, name: str):
        # validate the persons name and raise the appropriate error with the correct error message if needed
        pass

    def validate_person_address(self, address: str):
        # validate the persons address and raise the appropriate error with the correct error message if needed
        pass

    def validate_person_phone_number(self, phone_number: str):
        # validate the persons phone number and raise the appropriate error with the correct error message if needed
        pass

    def validate_person_email(self, email: str):
        if type(email) != str:
            raise TypeError(PersonMessages.INVALID_EMAIL)
        
        if not email:
            raise ValueError(PersonMessages.EMPTY_EMAIL)
        
        if len(email) > constants_messages.MAX_EMAIL_LENGTH:
            raise ValueError(PersonMessages.EMAIL_TOO_LONG)
        
        return email

    def dispose(self):
        pass
