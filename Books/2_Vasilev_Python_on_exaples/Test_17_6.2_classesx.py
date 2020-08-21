class MyClass:
    def __init__(self):
        self.number = 0

    def set(self, n):
        self.number = n
        print("Attention! Assigning a value!", n)

    def get(self):
        print('Field value:', self.number)


obj = MyClass()
obj.set(100)
obj.get()
