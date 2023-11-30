from person import Person
from person_validator import PersonValidator
from constants_messages import ContactBookMessages

class ContactBook:
    def __init__(self):
        self.contact_list: list[Person] = list()
        self.validator = PersonValidator()

    def add_contact(self, person: Person):
        # validate contact
        try:
            self.validator.validate_person_name(person.name)
            self.validator.validate_person_address(person.address)
            self.validator.validate_person_phone_number(person.phone_number)
            self.validator.validate_person_email(person.email)
        except:
            raise ValueError(ContactBookMessages.INVALID_ADD)
        
        # check for duplication
        if person in self.contact_list:
            raise Exception(ContactBookMessages.DUPLICATE_CONTACT)

        self.contact_list.append(person)

    def find_contact(self, name: str) -> Person:
        index = self._get_contact_index(name)
        
        return self.contact_list[index]

    def remove_contact(self, name: str):
        index = self._get_contact_index(name)
        
        self.contact_list.pop(index)

    def _get_contact_index(self, name: str) -> int:
        names = list(map(lambda x: x.name, self.contact_list))
        if name not in names:
            raise Exception(f'Contact {name} not in Contact Book.')
            
        return names.index(name)

    def __str__(self) -> str:
        return '\n'.join((str(person) for person in self.contact_list))