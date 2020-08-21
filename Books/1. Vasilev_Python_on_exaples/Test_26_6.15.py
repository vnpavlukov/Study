class ComplNum:
    def __init__(self, x=0, y=0):
        if type(x) == ComplNum:
            self.Re = x.Re
            self.Im = x.Im
        else:
            self.Re = x
            self.Im = y

    def show(self):
        print("Re =", self.Re)
        print("Im =", self.Im)


a = ComplNum(1, 2)
b = ComplNum(a)

print('A example:')
a.show()
print()
print('B example:')
b.show()
print()

print('Lets change a')
a.Re = 10
a.Im = 20

print('A example:')
a.show()
print()
print('B example:')
b.show()