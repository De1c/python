from collections import UserDict


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

    return inner


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        print('Address book recieved new record')

    def __repr__(self):
        return self.data


class Record:

    def __init__(self, name, phones = None):
        self.name = name
        self.phones = [phones]

    def add(self, phone):
        self.phones.append(Phone(phone))
        return f'Number {phone} has been added'

    def change(self, phone):
        for each_phone in self.phones:
            if Phone(phone) == each_phone:
                self.phones.remove(Phone(phone))
                self.add(Phone(phone))
                return f'Number {each_phone} has been changed for {phone}'
        return f'{phone} not found'


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):
    ...


class Phone(Field):
    ...


@input_error
def hello(book):
    return "How can I help you?"


@input_error
def add_rec(book, name, phone = None):

    book.add_record(Record(Name(name), Phone(phone)))
    return f'{name} has been added'


@input_error
def change(book, name, new_phone):
    book.data[Record(Name(name)).name.value].change(new_phone)
    return f'Number has been changed for '

@input_error
def show_phone(book, name):
    return book.data[Record(Name(name)).name.value].phones
    
    
@input_error
def show_all(book):
    return book.__repr__()


@input_error
def close(book):
    return 'Good bye'


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
        'good bye': close
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
            if len(spl_par) > 1:
                return operate(my_operation)(book, spl_par[0], spl_par[1])
            return operate(my_operation)(book, parameters)
        return operate(my_operation)(book)

    while True:
        user_input = input('Please enter command: ')
        output = handler(user_input)
        print(output)
        if output == 'Good bye':
            break


if __name__ == '__main__':
    main()
