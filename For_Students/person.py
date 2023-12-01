class Person:
    def __init__(self, name: str, address: str, phone_number: str, email: str):
        # initialize the class attributes
        pass
    
    @property
    def name(self) -> str:
        # get the given attribute
        pass
    
    @name.setter
    def name(self, name: str):
        # set the given attribute
        pass
    
    @property
    def address(self) -> str:
        # get the given attribute
        pass
    
    @address.setter
    def address(self, address: str):
        # set the given attribute
        pass
    
    @property
    def phone_number(self) -> str:
        # get the given attribute
        pass
    
    @phone_number.setter
    def phone_number(self, phone_number: str):
        # set the given attribute
        pass
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        self._email = email
    
    def __str__(self):
        # return the formatted person class attributes
        pass
    
    def __eq__(self, other):
        # determine if the other type is not identical to the Person class, and if so, return true
        if type(other) != Person:
            return False

        if (
            self.name == other.name and
            self.address == other.address and
            self.phone_number == other.phone_number and
            self.email == other.email
        ):
            return True

        return False
    
    def dispose(self):
        pass
