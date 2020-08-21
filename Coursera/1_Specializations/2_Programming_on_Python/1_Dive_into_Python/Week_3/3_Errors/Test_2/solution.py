import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        try:
            self.body_length, self.body_width, self.body_height = \
                [float(x) for x in self.body_whl.split('x')]
        except:
            self.body_length = self.body_width = self.body_height = float(0)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    file_formats = ['.jpg', '.jpeg', '.png', '.gif']

    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)

        for row in reader:
            if len(row) != 7:
                continue
            if os.path.splitext(row[3])[-1] not in file_formats:
                continue
            try:
                if row[0] == 'car' and float(row[5]) and row[1] and row[2]:
                    car = Car(row[1], row[3], row[5], row[2])
                    # print(row[1], row[3], row[5], row[2])
                    car_list.append(car)

                elif row[0] == 'truck' and row[1]:
                    truck = Truck(row[1], row[3], row[5], row[4])
                    # print(row[1], row[3], row[5], row[4])
                    car_list.append(truck)

                elif row[0] == 'spec_machine' \
                        and row[1] and float(row[5]) and row[6]:
                    spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
                    # print(row[1], row[3], row[5], row[6])
                    car_list.append(spec_machine)
            except:
                continue
    return car_list

# print(get_car_list('coursera_week3_cars.csv'))
