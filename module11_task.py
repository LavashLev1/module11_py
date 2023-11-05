from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass  # Ви можете додати логіку валідації в підкласах

class Phone(Field):
    def validate(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Неправильний формат номеру телефона")

class Birthday(Field):
    def validate(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Неправильний формат дати (РРРР-ММ-ДД)")

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday) if birthday else None

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            days_remaining = (next_birthday - today).days
            return days_remaining
        return None

class AddressBook:
    def __init__(self):
        self.contacts = []

    def iterator(self, chunk_size):
        for i in range(0, len(self.contacts), chunk_size):
            yield self.contacts[i:i + chunk_size]
