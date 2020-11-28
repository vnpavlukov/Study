"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""


class Clothes:
    def __init__(self, name):
        self.name = name
        self._area = None

    def area(self):
        pass

    def __str__(self):
        return f'нужно {self.area} метров ткани'


class Coat(Clothes):
    def __init__(self, name, size=0):
        super().__init__(name)
        self.size = size

    @property
    def area(self):
        if self._area is None:
            self._area = self.size / 6.5 + 0.5
        return self._area


class Suit(Clothes):
    def __init__(self, name, height=0):
        super().__init__(name)
        self.height = height

    @property
    def area(self):
        if self._area is None:
            self._area = 2 * self.height + 0.3
        return self._area


coat_1 = Coat('Снегурочка', 52)
suit_1 = Suit('Работник', 50)
print(coat_1)
print(suit_1)
total_materials = coat_1.area + suit_1.area
print(total_materials)
