import constants_messages
from constants_messages import PersonMessages

class PersonValidator:
    def __init__(self):
        pass

    def validate_person_name(self, name: str):
        if type(name) != str:
            raise ValueError(PersonMessages.INVALID_STRING)
        
        if not name:
            raise ValueError(PersonMessages.EMPTY_NAME)
        
        if len(name) > constants_messages.MAX_PERSON_NAME_LENGTH:
            raise ValueError(PersonMessages.NAME_TOO_LONG)
        
        return name

    def validate_person_address(self, address: str):
        if type(address) != str:
            raise ValueError(PersonMessages.INVALID_ADDRESS_TYPE)

        if not address:
            raise ValueError(PersonMessages.EMPTY_ADDRESS)
        
        if len(address) > constants_messages.MAX_ADDRESS_LENGTH:
            raise ValueError(PersonMessages.ADDRESS_TOO_LONG)
        
        return address

    def validate_person_phone_number(self, phone_number: str):
        if type(phone_number) != str:
            raise ValueError(PersonMessages.INVALID_PHONE_NUMBER_TYPE)
        
        if not phone_number:
            raise ValueError(PersonMessages.EMPTY_PHONE_NUMBER)
        
        if not phone_number.isdigit():
            raise ValueError(PersonMessages.INVALID_PHONE_NUMBER_TYPE)
        
        if len(phone_number) > constants_messages.PHONE_NUMBER_LENGTH:
            raise ValueError(PersonMessages.PHONE_NUMBER_WRONG_LENGTH)
        
        # return formatted phone number: (xxx)xxx-xxxx
        return f'({phone_number[:3]}){phone_number[3:6]}-{phone_number[6:10]}'

    def validate_person_email(self, email: str):
        if type(email) != str:
            raise ValueError(PersonMessages.INVALID_EMAIL)
        
        if not email:
            raise ValueError(PersonMessages.EMPTY_EMAIL)
        
        if len(email) > constants_messages.MAX_EMAIL_LENGTH:
            raise ValueError(PersonMessages.EMAIL_TOO_LONG)
        
        return email

    def dispose(self):
        pass