class Figure:
    def __init__(self, *args, **kwargs):
        self._area = None

    def get_area(self):
        return self._area

    def __str__(self):
        return f'{self.get_area()}'

    def __add__(self, other):
        instance = Figure()
        instance._area = self.get_area() + other.get_area()
        return instance


class Box(Figure):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self):
        if self._area is None:
            self._area = self.width * self.height
        return self._area


class Circle(Figure):
    def __init__(self, r, *args, **kwargs):
        super().__init__()
        self.r = r

    def get_area(self):
        if self._area is None:
            self._area = 3.14 * self.r ** 2
        return self._area


box_1 = Box(15, 20)
circle_1 = Circle(15)
print(box_1, circle_1)

all_data = box_1 + circle_1
print(all_data)