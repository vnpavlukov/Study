def func(a, b, c):
    return (a + b) * c


print(func(1, 3, 5))

print((lambda a, b, c: (a + b) * c)(1, 3, 5))
