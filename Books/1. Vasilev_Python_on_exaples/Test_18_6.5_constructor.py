class MyClass:
    def set(self, n):
        self.number = n
        print("Attention! Assigning a value!", n)

    def get(self):
        print('Field value:', self.number)

    def __init__(self, n=0):
        self.set(n)
        self.get()


a = MyClass()
print()
b = MyClass(99)
