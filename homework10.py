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

    def add_record(self, name, phone = None):
        record = Record(Name(name))
        phone = Phone(phone)
        self.data[Name(name)] = record
        if phone.value:
            record.add(phone)
            self.data[record.name.value] = record
        print('Address book recieved new record')
    
    
    def show_all(self):
        return self.data
    
class Record:
    
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add(self, phone):
        self.phones.append(Phone(phone))
        return f'Number {phone} has been added'
    
    def change(self, phone, old_phone):
        self.phones.remove(Phone(old_phone))
        self.phones.append(Phone(phone))
        return f'Number {old_phone} has been changed for {phone}'


    def phone(self):
        return f'Phone numbers for {self.name} is {self.phones}'

class Field:
    
    def __init__(self, value):
        self.value = value


class Name(Field):
    ...


class Phone(Field):
    ...


@input_error
def hello():
    return "How can I help you?"


@input_error
def close():
    return 'Good bye'



def main():
    
    book = AdressBook()

    OPERATIONS = {
        'hello': hello,
        'add': book.add_record,
        'add phone': book.data,
        'change': Record.change,
        'phone': Record.phone,
        'show all': book.show_all,
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
                return operate(my_operation)(spl_par[0], spl_par[1])
            return operate(my_operation)(parameters)
        return operate(my_operation)()

    while True:
        user_input = input('Please enter command: ')
        output = handler(user_input)
        print(output)
        if output == 'Good bye':
            break


if __name__ == '__main__':
    main()
