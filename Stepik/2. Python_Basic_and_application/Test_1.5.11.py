class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
print(a.val)
b = A()
print(b.val)
print()

a.bar()
print(a.val)
a.foo()
print(a.val)
print()

c = A()
print(c.val)
print()


print(a.val)
print(b.val)
print(c.val)