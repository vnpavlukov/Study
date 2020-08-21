class MyClass:
    name = 'Class MyClass'

    def set(self, n):
        self.nickname = n

    def get(self):
        print('Field name is:', self.nickname)

    def __init__(self, n):
        self.set(n)
        print('Created class instance')
        self.get()
