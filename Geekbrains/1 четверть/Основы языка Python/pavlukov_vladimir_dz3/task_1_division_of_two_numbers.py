"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division_of_two_numbers(first, second):
    if second == 0:
        return None
    else:
        return first / second


data_type = [
    [5, 0],
    [5, 2],
    [6, 2]
]

for data in enumerate(data_type):
    a, b = data[1]
    print(division_of_two_numbers(a, b))
