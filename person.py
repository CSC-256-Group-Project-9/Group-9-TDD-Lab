class Person:
    def __init__(self, name: str, address: str, phone_number: str, email: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}, Phone: {self.phone_number}, Email: {self.email}\n'
    
    def dispose(self):
        pass