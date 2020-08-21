class MyClass():
    def __init__(self, n):
        self.name = n

    def say(self):
        print('Class MyClass:', self.name)


A = MyClass('A')
B = MyClass('B')

A.say()
B.say()
print()

F = A.say
F()
print()

A.say = 'Field instance class A'
print(A.say)
print()

B.say()
print('This is F:')
F()
print()