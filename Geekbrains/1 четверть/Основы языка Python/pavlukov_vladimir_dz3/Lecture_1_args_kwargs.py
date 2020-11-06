def example(a, b, c):
    print(a * b * c)


example(1, 2, 3)  # positional *args
example(a=1, b=2, c=3)  # names **kwargs

kwargs = {'a': 1, 'b': 2, 'c': 3}  # зададим с помощь словаря
example(**kwargs)  # ** unpack the dict

args = [1, 2, 3]  # зададим с помощь списка
example(*args)  # ** unpack the list

print()
print('args:', args)  # [1, 2, 3]
print('*args:', *args)  # 1 2 3
print('equal:', 1, 2, 3)
print()

kwargs = {'a': 1, 'b': 2, 'c': 3}  # зададим с помощь словаря
print(*kwargs.values())  # 1 2 3
print(*kwargs.items())  # ('a', 1) ('b', 2) ('c', 3)


def calc_sum(*arguments):  # can not only unpack, but also pack
    result = 0
    for el in arguments:
        result += el
    return result
    # return sum(arguments)


print(calc_sum(1, 2, 3))
print()


def calc_sum(*arguments, **kwargs):
    print('args:', arguments)
    print('kwargs:', kwargs)


a = [1, 2, 3, 4]
calc_sum(*a)
print()

b = {'a': 1, 'b': 2}
calc_sum(**b)
calc_sum(a=1, b=1, c=1)
print()

calc_sum(15, 16, a=1, b=1, c=1)
print()


def show_product(**data):
    for key, val in data.items():
        print(f'{key} = {val}')


prod_1 = {'name': 15, 'sec': 4}
show_product(**prod_1)
