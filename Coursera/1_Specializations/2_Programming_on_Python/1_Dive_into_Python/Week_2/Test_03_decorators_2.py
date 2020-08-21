def first_dec(func):
    def wrapped():
        print('Inside first_dec product')
        return func()

    return wrapped


def second_dec(func):
    def wrapped():
        print('Inside second_dec product')
        return func()

    return wrapped


@first_dec
@second_dec
def decorated():
    print('Finally called!')


decorated()