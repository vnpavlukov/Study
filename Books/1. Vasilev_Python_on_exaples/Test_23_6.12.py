class MyClass():
    def __init__(self, n):
        self.name = n


A = MyClass('A')
B = MyClass('B')


def hello(argument_hello):
    print(argument_hello.name, 'Hello function')


def hi(argument_hi):
    print(argument_hi.name, 'Hi function')


MyClass.say = hello

A.say()
B.say()
print()

MyClass.say(A)
MyClass.say(B)
print()

MyClass.say = hi

A.say()
B.say()
print()

MyClass.say(A)
MyClass.say(B)
print()
