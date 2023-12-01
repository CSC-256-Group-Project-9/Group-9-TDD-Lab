from person import Person
from person_validator import PersonValidator
from constants_messages import ContactBookMessages

class ContactBook:
    def __init__(self):
        self.contact_list: list[Person] = list()
        self.validator = PersonValidator()

    def add_contact(self, person: Person):
        # validate contact and raise an error if needed
        pass

        # check for duplication and then add to the contact
        pass

    def find_contact(self, name: str) -> Person:
        # return the contact identified
        pass

    def remove_contact(self, name: str):
        # remove the contact from the contact_list
        index = self._get_contact_index(name)

        self.contact_list.pop(index)

    def _get_contact_index(self, name: str) -> int:
        # determine if the contact is in the contact book and return it
        pass

    def __str__(self) -> str:
        return '\n'.join((str(person) for person in self.contact_list))
