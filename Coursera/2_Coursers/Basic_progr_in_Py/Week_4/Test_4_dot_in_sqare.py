x = float(input())
y = float(input())


def dot_in_sqare(x, y):
    return ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5 <= \
           ((1 - 0) ** 2 + (1 - 0) ** 2) ** 0.5


if dot_in_sqare(x, y):
    print('YES')
else:
    print('NO')
