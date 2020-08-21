class summ_numbres:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value + 10


a = summ_numbres(20)
b = summ_numbres(30)
print(a + b)  # 60
