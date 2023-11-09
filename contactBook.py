from person import Person
from person_validator import PersonValidator

class ContactBook:
    def __init__(self):
        self.contact_list: list[Person] = list()
        self.validator = PersonValidator()

    def add_contact(self, person: Person):
        self.validator.validate_person_name(person.name)
        self.validator.validate_person_address(person.address)
        self.validator.validate_person_phone_number(person.phone_number)
        self.validator.validate_person_email(person.email)
        self.contact_list.append(person)

    def find_contact(self, name: str):
        pass

    def remove_contact(self, name: str):
        pass

    def __str__(self) -> str:
        return '\n'.join((str(person) for person in self.contact_list))