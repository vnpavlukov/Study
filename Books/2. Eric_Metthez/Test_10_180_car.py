from Test_9_179_car import Car, ElectricCar

audushechka = Car('audi', 'a4', 2016)
print(audushechka.get_descriptive_name())

audushechka.odometer_reading = 23
audushechka.read_odometr()
print()

my_tesla = ElectricCar('Tesla', 'Model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()