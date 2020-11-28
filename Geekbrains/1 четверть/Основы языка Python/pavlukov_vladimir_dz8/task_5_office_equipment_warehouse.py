"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь."""


class Warehouse:
    def __init__(self, equipment):
        self.equipment = equipment

    def add_equipment(self, name, count):
        self.equipment[name] = self.equipment[name] + count

    def allocate(self, name, count):
        self.equipment[name] = self.equipment[name] - count

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
