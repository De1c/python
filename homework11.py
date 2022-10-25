from collections import UserDict
import datetime
import re


def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name doesn't exist"
        except TypeError:
            return "Wrong command type"
        except IndexError:
            return "Input name and phone number"
        except ValueError:
            return "This name already exist"
        except ZeroDivisionError:
            return 'Wrong format'
    return inner


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name._value] = record
        print('Address book recieved new record')

    def iterator(self, count: int):
        i = 0
        while i < int(count):
            yield list(self.data.items())[i]
            i += 1

    def __repr__(self):
        return self.data


class Record:

    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        self.phones = [phones]
        self.birthday = birthday

    def add(self, phone):
        self.phones.append(Phone(phone))
        return f'Number {phone} has been added'

    def days_to_birthday(self):
        today = datetime.date.today()
        my_birthday = datetime.date(today.year, int(self.birthday._value.split('.')[1]), int(self.birthday._value.split('.')[0]))
        if my_birthday == today:
            return "Happy Birthday!"
        else:
            if my_birthday < today:
                my_birthday = my_birthday.replace(year=today.year + 1)
                return f'Days until birhday: {my_birthday - today}'
            return f'Days until birhday: {my_birthday - today}'

    def change(self, old_phone, new_phone):
        for each_phone in self.phones:
            if Phone(old_phone) == each_phone:
                self.phones.remove(Phone(old_phone))
                self.add(Phone(new_phone))
                return f'Number {each_phone} has been changed for {new_phone}'
        return f'{old_phone} not found'


class Field:

    def __init__(self, value):
        self._value = value

    


class Birthday(Field):


    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_birthday):
        if not new_birthday:
            pass
        else:
            new_birthday_clear = new_birthday.strip()
            match = re.fullmatch(r'\d{2}[.]\d{2}[.]\d{4}', new_birthday_clear)
            if match and len(new_birthday_clear) == 10:
                self._value = new_birthday_clear
            else:
                print('Wrong birthday format, try: DD.MM.YYYY')
                raise ZeroDivisionError

class Name(Field):
    ...


class Phone(Field):

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_phone):
        if not new_phone:
            pass
        else:
            phone_clear = new_phone.strip()
            match = re.fullmatch(r'[+]\d{1,}', phone_clear)
            if match:
                self._value = phone_clear
            else:
                print('Wrong phone number format, try: +0123456789')
                raise ZeroDivisionError


@input_error
def hello(book):
    return "How can I help you?"

@input_error
def add_rec(book, name, phone=None, birthday=None):

    book.add_record(Record(Name(name), Phone(phone), Birthday(birthday)))
    return f'{name} has been added'


@input_error
def change(book, name, old_phone, new_phone):
    book.data[name].change(old_phone, new_phone)
    return f'Number {old_phone} has been changed for {new_phone}'


@input_error
def show_phone(book, name):
    return book.data[name].phones


@input_error
def show_all(book):
    return book.__repr__()


@input_error
def close(book):
    return 'Good bye'


@input_error
def days_to_birthday(book, name):
    return book.data[name].days_to_birthday()


def show_n_records(book, count: int):
    return [i for i in book.iterator(count)]


def main():

    book = AdressBook()

    OPERATIONS = {
        'hello': hello,
        'add': add_rec,
        'change': change,
        'phone': show_phone,
        'show all': show_all,
        'exit': close,
        'close': close,
        'good bye': close,
        'birthday': days_to_birthday,
        'show': show_n_records
    }

    def operate(user_input):
        return OPERATIONS.get(user_input)

    def handler(user_input):

        my_operation = None
        parameters = ''
        for operation in OPERATIONS:
            if user_input.lower().startswith(operation):
                my_operation = operation
                parameters = user_input[len(operation):]
                break
        if parameters:
            spl_par = parameters.split()
            if my_operation == 'change':
                return operate(my_operation)(book, spl_par[0], spl_par[1], spl_par[2])
            if len(spl_par) > 2:
                return operate(my_operation)(book, spl_par[0], spl_par[1], spl_par[2])
            if len(spl_par) > 1:
                return operate(my_operation)(book, spl_par[0], spl_par[1])
            return operate(my_operation)(book, parameters.strip())
        return operate(my_operation)(book)

    while True:
        user_input = input('Please enter command: ')
        output = handler(user_input)
        print(output)
        if output == 'Good bye':
            break


if __name__ == '__main__':
    main()
