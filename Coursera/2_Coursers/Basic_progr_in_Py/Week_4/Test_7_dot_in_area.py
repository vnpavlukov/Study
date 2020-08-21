x_1 = float(input())
y_1 = float(input())


def IsPointInArea(x, y):
    return (x + 1) ** 2 <= 2 ** 2 - (y - 1) ** 2 and \
           x >= -y and 2 * x <= y - 2 or \
           (x + 1) ** 2 >= 2 ** 2 - (y - 1) ** 2 and \
           x <= -y and 2 * x >= y - 2


if IsPointInArea(x_1, y_1):
    print('YES')
else:
    print('NO')
