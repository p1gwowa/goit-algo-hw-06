from collections import UserDict

class Field:                                                            # Class Field for input value
    def __init__(self, value):                                          # Construction of class 
        self.value = value

    def __str__(self):                                                  # Magic method
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    

class Name(Field):                                                      # Class Name for creating name for Address Book
    def __init__(self, name=None):                                      # Construction of class with condition
        if name is None:
            raise ValueError
        super().__init__(name)


class Phone(Field):                                                     # Class Phone for creating of phone num for Address Book
    def __init__(self, phone):                                          # Construction of class with condition
        if len(phone) != 10:
            raise ValueError
        super().__init__(phone)
   
class Record:                                                           # Class Record for creating methods for operation with Address Book
    def __init__(self, name):                                           # Construction of class
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone):                                         # Method for adding phone num
        if self.find_phone(phone):
            return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):                                      # Method for removing phone num
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
            return
        raise ValueError
    
    def edit_phone(self, old_phone, new_phone):                         # Method for editting existing phone num 
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
            return
        raise ValueError

    def find_phone(self, phone):                                        # Method for finding phone num in list of phones       
        for p in self.phones:
            if p.value == phone:
                return p
            
    def __str__(self):                                                  # Magic methods
        return f'Record(Name: {self.name} Phones: {self.phones})'
    
    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'

           
class AddressBook(UserDict):                                            # Class Address Book (main operational class) for saving information in it
    def add_record(self, record: Record):                               # Method for adding Record in Address Book
        name = record.name.value
        self.data.update({name: record})

    def find(self, name):                                               # Method for finding Record in Address Book
        return self.get(name)
    
    def delete(self, name):                                             # Method for removing Record in Address Book
        del self[name]


if __name__ == '__main__':                                              # Main condition
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

