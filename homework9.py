my_dict = {}

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

@input_error
def hello():
    return "How can I help you?"


@input_error
def add(name_ph_number):
    
    splited = name_ph_number.split()
    name = splited[0]
    ph_number = splited[1]
    if name in my_dict:
        raise ValueError
    my_dict[name] = ph_number
    return f'{name} has been added'

@input_error
def change(name_ph_number):
    
    splited = name_ph_number.split()
    name = splited[0]
    new_number = splited[1]
    old_number = my_dict[name]
    my_dict[name] = new_number
    return f'Number {old_number} has been changed for {new_number}'


@input_error
def phone(name):
    return f'Phone number for {name} is {my_dict[name]}'
    

@input_error
def show_all():
    
    my_string = ''
    for name, phone in my_dict.items():
        my_string += f'{name}, {phone}\n'
    return my_string


@input_error
def close():
    return 'Good bye'

OPERATIONS ={'hello': hello,
            'add' : add,
            'change' : change,
            'phone' : phone,
            'show all' : show_all,
            'exit' : close,
            'close' : close,
            'good bye' : close
            }
@input_error
def operate(user_input):
    return OPERATIONS.get(user_input)

@input_error
def handler(user_input):
    
    my_operation = None
    parameters = ''
    for operation in OPERATIONS:
        if user_input.lower().startswith(operation):
            my_operation = operation
            parameters = user_input[len(operation):]
            break
    if parameters:
        return operate(my_operation)(parameters)
    return operate(my_operation)()

@input_error
def main():
    
    while True:
        user_input = input('Please enter command: ')
        output = handler(user_input)
        print(output)
        if output == 'Good bye':
            break

if __name__ == '__main__':
    main()