from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, first_name, last_name=None):
        if last_name:
            super().__init__(f"{first_name} {last_name}")
        else:
            super().__init__(first_name)

class Phone(Field):
    def __init__(self, value):
        if self._validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number format")

    def _validate_phone(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(*name.split())
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        return f" Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)} "

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


book = AddressBook()    # Створення нової адресної книги

                        # Створення запису для John
john_record = Record("John Doe")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


book.add_record(john_record)    # Додавання запису John до адресної книги

                                # Створення та додавання нового запису для Jane
jane_record = Record("Jane Smith")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items(): # Виведення всіх записів у книзі
    print(record)


john = book.find("John Doe")     # Знаходження та редагування телефону для John
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John Doe, phones: 1112223333; 5555555555


found_phone = john.find_phone("5555555555")  # Пошук конкретного телефону у записі John
print(f" \n {found_phone} this is {john.name} phone number ")   # Виведення: 5555555555


book.delete("Jane Smith") # Видалення запису Jane

# перевіримо чи видалили запис через всіх хто є у книзі
#for name, record in book.data.items(): 
#    print(record)

#  проверка на ошибку 
sharon_record = Record("Sharon Stone")
sharon_record.add_phone("3333338888")
# sharon_record.add_phone("22222222")
book.add_record(sharon_record)


#  перевіримо чи додався запис через всіх хто є у книзі
for name, record in book.data.items(): 
    print(record)