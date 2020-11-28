class Box:
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        self.color = color
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = self.width * self.height
        return self._area

    def __str__(self):
        return f'{self.area}'

    def __add__(self, other):
        return Box(self.width + other.width, self.height + other.height)


box_1 = Box(15, 20)
box_2 = Box(20, 5)
box_3 = Box(15, 25)

box_summ = box_1 + box_2 + box_3
print(box_summ.area)
print(box_summ)
