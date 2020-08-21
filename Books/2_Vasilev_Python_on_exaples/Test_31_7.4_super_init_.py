class BaseClass:
    def __init__(self, num):
        self.id = num

    def get(self):
        print("ID:", self.id)

    def show(self):
        print("Field instance the base class")
        self.get()


class NewClass(BaseClass):
    def __init__(self, num, txt):
        super().__init__(num)
        self.name = txt

    def get(self):
        super().get()
        print("Name:", self.name)

new_base = BaseClass('Vova')
new_base.show()
print()

new_class = NewClass(10, 'ten')
new_class.show()
