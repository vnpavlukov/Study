class Alpha:
    def hi():
        print('Class Alpha')


class Bravo:
    def hi():
        print('Class Bravo')


class Charlie:
    def hi():
        print('Class Charlie')


class Delta(Alpha):
    pass


class Echo(Delta):
    pass


class Foxtron(Bravo, Alpha):
    pass


class Golf(Foxtron):
    pass


class Hotel(Echo, Charlie, Golf):
    pass


Echo.hi()  # Delta, Alpha
Golf.hi()  # Foxtron, Bravo
Hotel.hi()  # Echo, Delta, Charlie, Golf, Foxtrot

print(Hotel.__mro__)