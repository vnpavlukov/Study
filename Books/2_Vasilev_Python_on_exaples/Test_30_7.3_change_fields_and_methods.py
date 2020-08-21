class BaseClass:
    name = "Field name of BaseClass"

    def say(self):
        print('Method say() of BasicClass\n')


class NewClass(BaseClass):
    name = "Field name of NewClass"

    def say(self):
        print('Method say() of NewClass')


obj_base = BaseClass()
obj_new = NewClass()

print(obj_base.name)
obj_base.say()

print(obj_new.name)
obj_new.say()
