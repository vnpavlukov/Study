class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = PowTwo(3)

for i in numbers:
    print(i)
print()


class InfIter:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num < 10:
            num = self.num
            self.num += 2
            return num
        else:
            raise StopIteration


numbers = InfIter()
for i in numbers:
    print(i)


class Count:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num
