class MyClass:
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt

    def __len__(self):
        return len(self.txt)

    def __index__(self):
        return self.txt.count(' ') + 1

    def __round__(self):
        self.txt = "Сброс значений"
        return self


txt = 'one and two and three and four'
txt += '\ngo the rabbit on the floor'

print(txt)
print()

obj = MyClass(txt)
print(obj)
print(len(obj))

print(obj.__index__())
print(bin(obj))
print(oct(obj))
print(hex(obj))
print(round(obj))
print(obj)