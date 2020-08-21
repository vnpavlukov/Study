def dec(func):
    return func


@dec
def decorated():
    print('Hi!')


decorated()
