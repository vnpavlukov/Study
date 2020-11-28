def my_decor(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"calls: {counter}")
        return func(*args, **kwargs)

    return wrapper


@my_decor
def say_hello(name):
    print(f'Hello {name}\n')


say_hello('Ivan')
say_hello('Vova')
