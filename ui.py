from contactBook import ContactBook
from constants_messages import UIMessages
from person import Person

class CLI:
    def __init__(self, contact_book: ContactBook):
        self.contact_book = contact_book

    def display_menu(self):
        return ("Menu:\n"
                "1. Add Contact\n"
                "2. Remove Contact\n"
                "3. List Contacts\n"
                "4. Exit\n")

    def main_loop(self):
        while True:
            print(self.display_menu())

            choice = input('> ')

            match choice:
                case '1':
                    self.add_contact()
                case '2':
                    self.remove_contact()
                case '3':
                    print(self.display_list())
                case '4':
                    break
                case _:
                    print(UIMessages.INVALID_MENU_OPTION)

    
    def check_input(self, user_input: str) -> bool:
        if not user_input.isdigit():
            return False
        
        if int(user_input) not in (1, 2, 3, 4):
            return False
        
        return True

    def add_contact(self):
        try:
            name = self.contact_book.validator.validate_person_name(input('full name: '))
            address = self.contact_book.validator.validate_person_address(input('street address: '))
            phone_number = self.contact_book.validator.validate_person_phone_number(input('phone number: '))
            email = self.contact_book.validator.validate_person_address(input('email address: '))
        except Exception as err:
            print(err)
            return

        person = Person(name=name,
                        address=address,
                        phone_number=phone_number,
                        email=email)

        try:
            self.contact_book.add_contact(person=person)
        except Exception as err:
            print(err)

    def remove_contact(self):
        name = input('full name: ')

        try:
            self.contact_book.remove_contact(name=name)
        except Exception as err:
            print(err)

    def display_list(self):
        if self.contact_book.contact_list:
            return ''.join([str(person) + '\n' for person in self.contact_book.contact_list])
        
        return UIMessages.EMPTY_CONTACT_BOOK


if __name__ == "__main__":
    CLI(ContactBook()).main_loop()