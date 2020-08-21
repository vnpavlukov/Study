class Human:
    pass


class Robot:
    """Create robots"""


print(Robot)
print(dir(Robot))
print()


class Planet:
    pass


Mars = Planet()
print(Mars)
print()

solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print('solar_system:', solar_system)


class Planet:
    def __init__(self, name):
        self.name = name


earth = Planet('Earth')
print(earth.name)  # Earth
print(earth)  # <__main__.Planet object at 0x02C0E880>


class Planet:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


print(earth)  # Earth
