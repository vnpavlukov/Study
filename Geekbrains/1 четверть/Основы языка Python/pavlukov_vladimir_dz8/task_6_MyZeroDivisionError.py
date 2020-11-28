"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП."""


class CheckOnNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, equipment):
        self.equipment = equipment

    def add_equipment(self, name, count):
        try:
            if not str(count).isdigit():
                raise CheckOnNumbers('Count must be a number')
            self.equipment[name] = self.equipment[name] + count
        except CheckOnNumbers as err:
            print(err)

    def allocate(self, name, count):
        try:
            if not str(count).isdigit():
                raise CheckOnNumbers('Count must be a number')
            self.equipment[name] = self.equipment[name] - count
        except CheckOnNumbers as err:
            print(err)

    def amountOf(self, name):
        return f'"{name.name}" {self.equipment[name]} штук'


class OfficeAppliances:
    def __init__(self, name, price):
        self.name = name
        self.prise = price


class Printer(OfficeAppliances):
    def __init__(self, name, price, amount_paper_tray):
        super().__init__(name, price)
        self.amount_paper_tray = amount_paper_tray


class Scanner(OfficeAppliances):
    def __init__(self, name, price, copy_resolution):
        super().__init__(name, price)
        self.copy_resolution = copy_resolution


class Copier(OfficeAppliances):
    def __init__(self, name, price, max_format):
        super().__init__(name, price)
        self.max_format = max_format


hp = Printer('hp 2000', 7500, 1000)
canon = Scanner('Canon z5', 6500, '1600*2800')
xerox = Copier('Xerox C110', 27500, 'A1')

warehouse1 = Warehouse({hp: 5, canon: 3, xerox: 2})
warehouse1.add_equipment(hp, 5)
warehouse1.allocate(hp, 2)
print(warehouse1.amountOf(hp))
