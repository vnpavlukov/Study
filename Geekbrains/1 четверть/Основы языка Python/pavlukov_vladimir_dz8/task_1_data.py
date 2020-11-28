"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
 «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
 извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
 должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
 структуры на реальных данных."""


class Date:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def get_data_in_int(cls, date_in_str):
        return [int(i) for i in date_in_str.split('-')]

    @staticmethod
    def validate(date_in_str):
        day, month, year = date_in_str.split('-')
        return int(day) < 32 and 0 < int(month) < 13 and int(year) > 0


today = Date('24-11-2020')
print(Date.get_data_in_int('24-11-2020'))
print(Date.validate('24-11-2020'))
