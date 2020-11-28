"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой."""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division_two_num(a, b):
    try:
        if b == 0:
            raise MyZeroDivisionError("Вы ввели отрицательное число!")
    except MyZeroDivisionError as err:
        print(err)
    else:
        print(a / b)


division_two_num(6, 3)
division_two_num(6, 0)
