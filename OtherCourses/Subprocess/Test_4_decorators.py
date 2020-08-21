def say_hello(name):
    return f'Hello, {name}!'


def be_awesome(name):
    return f"Cool, {name}, be together so cool"


def greet_vanya(greeter_func):
    return greeter_func('Vanya')


print(greet_vanya(say_hello))
print(greet_vanya(be_awesome))
print()


def parent():
    print('Hello it`s parent()')

    def first_child():
        print('First child')

    def second_child():
        print('Second child')

    second_child()
    first_child()


parent()
