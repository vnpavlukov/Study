class BoxSize:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def show(self):
        print('Sizes of the box:\n',
              '\tWibth:', self.width, "\n",
              '\tHeight:', self.height, '\n',
              '\tDepth:', self.depth, '\n',
              '\tVolume:', self.volume())


class BoxParams:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def show(self):
        print('Additional box parameters:\n',
              '\tWeight (mass):', self.weight, '\n',
              '\tColor:', self.color)


class Box(BoxSize, BoxParams):
    def __init__(self, width, height, depth, weight, color):
        BoxSize.__init__(self, weight, height, depth)
        BoxParams.__init__(self, weight, color)
        self.show()

    def show(self):
        BoxSize.show(self)
        BoxParams.show(self)


MyBox = Box(10, 20, 30, 5, 'creen')
