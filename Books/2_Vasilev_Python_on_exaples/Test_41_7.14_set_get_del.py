class MyClass:
    def __setattr__(self, key, value):
        print('Making method __setattr__():')
        txt = "*\Field " + str(key)
        txt += ' assigning a value ' + str(value)
        print(txt)
        self.__dict__[key] = value
        print('Method __setattr__() is made.')

    def __getattribute__(self, item):
        print('Is currently running __getattribute__() method:')
        txt = '*\treading the field value ' + str(item)
        print(txt)

        try:
            res = object.__getattribute__(self, item)
        except AttributeError:
            res = 'For the instance of the field ' + str(item) + ' no!'
            print('Method __getattribute__() is finishing')
            return res

    def __delattr__(self, item):
        print('Method __delattr__() is starting:')
        txt = "*\t deleting the field " + str(item)
        print(txt)
        try:
            del self.__dict__[item]
        except KeyError:
            print("We can't delete this field " + str(item))
        print("Method __delattr__() is finished.")


obj = MyClass()
obj.name = "Python"
print("Attribute field name:", obj.name, '\n')

del obj.name
print(obj.name)

del obj.name