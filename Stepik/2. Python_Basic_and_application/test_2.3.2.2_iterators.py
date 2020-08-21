from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __next__(self):
        if self.n > self.i:
            self.i += 1
            return random()
        else:
            raise StopIteration


for x in RandomIterator(10):
    print(x)
