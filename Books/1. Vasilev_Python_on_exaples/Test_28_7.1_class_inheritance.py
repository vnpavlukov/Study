class BaseClass:
    name_base = 'Class BaseClass'

    def say_base(self):
        print('Method say_base() \n')


class NewClass(BaseClass):
    name_new = 'Class NewClass'

    def say_new(self):
        print('Method say_new() \n')


obj_base = BaseClass()
obj_new = NewClass()

print("Class BaseClass and instance obj_base:")
print(BaseClass.name_base)

obj_base.say_base()

print("Class NewClass and instance obj_new:")
print(NewClass.name_base)
print()

obj_new.say_base()
print(NewClass.name_new)
obj_new.say_new()

obj_new.say_base()
obj_new.say_new()