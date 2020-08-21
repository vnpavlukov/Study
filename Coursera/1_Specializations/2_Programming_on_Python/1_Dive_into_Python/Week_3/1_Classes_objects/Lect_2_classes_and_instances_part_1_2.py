class Planet:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


solar_system = []

planet_names = [
    'Merc', 'Ven', 'Earth', 'Mars',
    'Jup', 'Sat', 'Ur', 'Nept'
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
