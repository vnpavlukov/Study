def make(func):
    def inner():
        print('Hi')
        func()

    return inner


@make
def ordinary():
    print('Hello')


ordinary()
print()


def divide(a, b):
    print(a / b)


divide(2, 5)
print()


def smart_divide(func):
    def inner(a, b):
        print('I want to divide two numbers')
        if b == 0:
            print('You can\`t do it')
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
divide(2, 0)