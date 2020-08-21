x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
r = float(input())


def IsPointInCircle(x_1, y_1, x_2, r):
    return r - ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5 >= 0


if IsPointInCircle(x_1, y_1, x_2, r):
    print('YES')
else:
    print('NO')
