from copy import copy, deepcopy


class MyClass:
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums

    def show(self):
        print('name:', self.name)
        print('nums:', self.nums, '\n')


x = MyClass('Python', [1, 2, 3])
print('Class instance x:')
x.show()

y = copy(x)
z = deepcopy(x)

print('Class  instance y:')
y.show()

print('Class  instance z:')
z.show()

print('Change x name in Java, and num[0] on 0 \n ')
x.name = 'Java'
x.nums = 0

print('Class  instance x:')
x.show()
print('Class  instance y:')
y.show()
print('Class  instance z:')
z.show()