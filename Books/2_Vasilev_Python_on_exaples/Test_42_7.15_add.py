class Adder:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return 'Number is: ' + str(self.number)

    def __add__(self, other):
        return Adder(self.number + other)


a = Adder(10)
b = a + 5

print(a)
print(b)
