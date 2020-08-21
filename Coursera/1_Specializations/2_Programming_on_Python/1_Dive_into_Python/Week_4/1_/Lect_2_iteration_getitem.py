class Iterator:  # итерация по заданному условию
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):  # всегда возвращает себя
        return self

    def __next__(self):  # определяет какие методы возвращаются при итерации
        if self.current >= self.end:
            raise StopIteration

        result = self.current + 2
        self.current += 1
        return result


for num in Iterator(1, 5):
    print(num)


class IndexIterable:  # итерация по индексу метода
    def __init__(self, name):
        self.name = name

    def __getitem__(self, index):
        return self.name[index]


Vova = IndexIterable('Vova')

for letter in Vova:
    print(letter)
