from random import random


class RandomIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __next__(self):
        if self.n > self.i:
            self.i += 1
            return random()
        else:
            raise StopIteration


x = RandomIterator(3)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
