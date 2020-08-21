class MyClass:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def dec(self):
        self.count += 1

x = MyClass()
print(x.count)
x.inc()
print(x.count)