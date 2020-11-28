"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости."""


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.direction_of_movement = 'север'

    def go(self):
        return f'транспорт поехала'

    def stop(self):
        return f'транспорт остановилась'

    def turn(self, direction):
        return f'транспорт повернул: {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
            return self.speed
        else:
            return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
            return self.speed
        else:
            return self.speed


class PoliceCar(Car):
    is_police = True


School_bus = TownCar(61, 'red', 'o000oo')
print(School_bus.show_speed())

Vasya_speedy = SportCar(80, 'red', 'o000oo')
print(Vasya_speedy.go())

Grisha_Taxi = WorkCar(80, 'yellow', 'x744av')
print(Grisha_Taxi.stop())

Petr_MVD = WorkCar(80, 'yellow', 'x744av')
print(Petr_MVD.turn('направо'))
