class MyClass:
    Nmax = 5

    def __init__(self):
        n = MyClass.Nmax
        self.nums = [0 for i in range(n)]

    def __str__(self):
        txt = '|'
        for s in self.nums:
            txt += ' ' + str(s) + ' |'
        return txt

    def __setitem__(self, key, value):
        k = key % len(self.nums)
        self.nums[k] = value

    def __getitem__(self, item):
        k = item % len(self.nums)
        return self.nums[k]

    def __delitem__(self, key):
        k = key % len(self.nums)
        self.nums[k] = '*'


obj = MyClass()
print(obj)

obj[0], obj[2], obj[24] = 100, -3, 123

print(obj, '\n')
print(obj[0], obj[1], obj[2], obj[3], obj[4], obj[44])

del obj[0]

print(obj)

del obj[9]

print(obj)
