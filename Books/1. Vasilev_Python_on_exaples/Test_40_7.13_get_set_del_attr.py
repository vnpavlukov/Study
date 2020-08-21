class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + ' caramba'

    def __setattr__(self, key, value):
        if key == 'name':
            self.__dict__[key] = value
        else:
            print('You can`t do this')

    def __getattr__(self, item):
        return 'There is no such of field'

    def __delattr__(self, item):
        print('You can`t delete the field')


obj = MyClass('Original Value')  # because __str__ return name
print(obj)
obj.name = 'new name'
print(obj)
obj.namber = 100