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

    def add(self, other):
        new_box = Box(self.width + other.width, self.height + other.height)
        return new_box


box_1 = Box(15, 20)
box_2 = Box(20, 5)
box_3 = Box(15, 25)

box_summ = box_1.add(box_2)
print(box_summ)
