class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __call__(self):
        volume = self.width * self.height * self.depth
        print('Volume equal:', volume)


box_1 = Box(10, 20, 30)
box_1()
