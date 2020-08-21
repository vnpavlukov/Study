class MyClass:
    name = "Class MyClass"

    def set(self, n):
        self.nickname = n
        print("Attention! Assigning a nickname!", n)

    def get(self):
        print('Nickname value:', self.nickname)

    def __init__(self, n=0):
        self.set(n)
        print('created class instance')
        self.get()


green = MyClass('Green')
print()
red = MyClass('Red')

MyClass.name = 'Here can be your advertising'
