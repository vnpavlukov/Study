class MyClass:
    pass


A = MyClass()
B = MyClass()
C = MyClass()


def hello():
    print('Method instance - hello')


def hi():
    print('Enover method - hi')

A.say = hello
C.say = hi

C.say()
