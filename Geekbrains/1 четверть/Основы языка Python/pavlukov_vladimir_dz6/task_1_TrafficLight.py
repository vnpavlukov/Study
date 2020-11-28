"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод."""

from time import sleep


class TrafficLight:
    def __init__(self):
        self.color = 'красный'

    def run(self, red_time=7, yellow_time=3, green_time=2):
        while True:
            if self.color == 'красный':
                print(f'Now is {self.color} {red_time} seconds')
                sleep(red_time)
                self.color = 'желтный'

            elif self.color == 'желтный':
                print(f'Now is {self.color} {yellow_time} seconds')
                sleep(yellow_time)
                self.color = 'зеленый'

            elif self.color == 'зеленый':
                print(f'Now is {self.color} {green_time} seconds')
                sleep(green_time)
                self.color = 'красный'


lenina_trafficLight = TrafficLight()
lenina_trafficLight.run()
