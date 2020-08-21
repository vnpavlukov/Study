x_1 = float(input())
y_1 = float(input())


def dot_in_rhombus(x, y):
    return x <= -y + 1 and x >= -y - 1 and x >= y - 1 and x <= y + 1


if dot_in_rhombus(x_1, y_1):
    print('YES')
else:
    print('NO')
