def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call the func')
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('After call the func')

    return wrapper


@my_decorator
def say_whee(name):
    print(f'Yeah! {name}')


valera = say_whee('Valera')
peas = say_whee('World')

valera
peas
print()


@my_decorator
def return_greeting(name):
    print('Ready to greeting')
    return f'Hello, {name}'


adam = return_greeting('Adam')
print(adam)
print()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call Adam')
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def return_greeting(name):
    print('Ready to greeting')
    return f'Hello, {name}'


adam = return_greeting('Adam')
print(adam)
