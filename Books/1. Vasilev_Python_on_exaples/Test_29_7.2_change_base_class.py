class BaseClass:
    name = 'Field name'

    def say(self):
        print('Method say()\n')


class NewClass(BaseClass):
    pass


obj = NewClass()
print(NewClass.name)
obj.say()


def hello(self):
    print("New method hello()")


BaseClass.say = hello
obj.say()

BaseClass.name = "This is new field"
print(NewClass.name)

BaseClass.name = hello
obj.name()