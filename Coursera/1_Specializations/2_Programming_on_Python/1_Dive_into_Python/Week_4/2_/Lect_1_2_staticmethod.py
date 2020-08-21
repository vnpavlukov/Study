class Descriptor:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, instance, owner):
        print('get')
        return self.value

    def __set__(self, instance, value):
        self.value = self._prepare_value(value)
        print(self.value)


class Class:
    attr = Descriptor()


instance = Class()

instance.attr = 10

