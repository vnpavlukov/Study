"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class Warehouse:
    def __init__(self, equipment):
        self.equipment = equipment


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
warehouse = Warehouse({hp: 5, canon: 3, xerox: 2})
