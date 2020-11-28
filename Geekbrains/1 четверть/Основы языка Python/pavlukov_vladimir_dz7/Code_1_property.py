class Box:
    def __init__(self, width, height, color=None):
        self.width = width
        self.height = height
        self.color = color
        self._area = None

    def area(self):
        if self._area is None:
            self._area = self.width * self.height
        return self._area


box_1 = Box(15, 20)
print(box_1.area())


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


box_1 = Box(15, 20)
print(box_1.area)
