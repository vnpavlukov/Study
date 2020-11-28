"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу
метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т."""


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_weight_asphalt(self, weight, thickness):
        return weight * thickness * self.length * self.width


lenina_road = Road(5000, 20)
print(f'{lenina_road.calculate_weight_asphalt(5, 25) / 1000 :.0f} т')
