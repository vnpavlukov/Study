def func_get(name_space, arg):
    for n in name_space.values():
        if arg in n:
            return 'хуета'
        return 'None'


values = (
    ({'a': [1, 2, 3]}, 2),
    ({'b': (1, 2, 3)}, 4),
 #   ({'c': 1}, 1)
)

for a, b in values:
    print(func_get(a, b))

d = {'dict': 1, 'dictionary': 2}

for i in d.values():
    print(i)
