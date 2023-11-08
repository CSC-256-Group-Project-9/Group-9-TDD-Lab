from person import Person

class contactBook(object):

    # Deafault Constructor
    def __init__(self):
        self.contacts = []

    #len dunder
    def __len__(self):
        return len(self.contacts)
   
    # str dunder
    def __str__(self):
        return ", ".join(map(str, self))
   
    # iter dunder
    def __iter__(self):
        """Supports iteration over contact book"""
        cursor = 0
        while cursor < len(self):
            yield self.contacts[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        result = list(self)
        for item in other:
            result.append(item)
        return result
    
    # add a contact of type Person
    def add_contact(self, contact: Person):
        self.contacts.append(contact)
    
#Main function for testing (well the test before running the Test script)   
def main():
    
    ant = Person
    ant.name = "Anthony"
    ant.address = "123 I Live Here Lane"
    ant.phone_number = "(123)456-8910"

    book = contactBook

    book.add_contact(ant)

    print(book)




if __name__ == "__main__":
    main()