class MyClass:
    name = 'Class MyClass'

    def __init__(self, n):
        self.set(n)
        print('The instance of the class was created')
        self.get()  # print the value of field

    def set(self, n):  # method for assigning a name
        self.nickname = n

    def get(self):  # method for get the name of field
        print('Field value:', self.nickname)


green = MyClass('Green')
print(green.name)

red = MyClass('Red')
print(red.name)

green.name = 'Here was green'

print()
print(red.name)
print(green.name)

MyClass.name = 'Here can be you advertising'
print()
print(red.name)
print(green.name)

del green.name
print()
print(green.name)