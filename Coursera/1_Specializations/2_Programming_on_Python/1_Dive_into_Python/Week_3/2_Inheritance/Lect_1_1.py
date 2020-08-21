class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return '{0}: waw'.format(self.name)


Doberman_Sharik = Dog('Шарик', 'Доберман')
print(Doberman_Sharik.name)
print(Doberman_Sharik.breed)
print(Doberman_Sharik.say())

print(Dog.__mro__)
