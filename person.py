class Person:
    def __init__(self, name: str, address: str, phone_number: str, email: str):
        self._name = name
        self._address = address
        self._phone_number = phone_number
        self._email = email
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, address: str):
        self._address = address
    
    @property
    def phone_number(self) -> str:
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number: str):
        self._phone_number = phone_number
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        self._email = email
    
    def __str__(self):
        return (
            f'Name: {self.name}, '
            f'Address: {self.address}, '
            f'Phone: ({self.phone_number[:3]}){self.phone_number[3:6]}-{self.phone_number[6:10]}, '  # (xxx)xxx-xxxx
            f'Email: {self.email}'
        )
    
    def dispose(self):
        pass