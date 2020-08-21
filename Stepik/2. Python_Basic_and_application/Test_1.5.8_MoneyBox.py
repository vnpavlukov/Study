class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return bool(self.capacity - v >= 0)

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v


x = MoneyBox(15)
print(x.capacity)
print()

x.add(5)
print(x.capacity)
print(x.can_add(1))
print()

x.add(9)
print(x.capacity)
print(x.can_add(2))