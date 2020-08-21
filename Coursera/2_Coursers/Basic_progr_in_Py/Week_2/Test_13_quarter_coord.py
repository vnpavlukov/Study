x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def sing_number(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0


def check_dots(x_1, y_1, x_2, y_2):
    if sing_number(x_1) == sing_number(x_2) and \
            sing_number(y_1) == sing_number(y_2):
        return "YES"
    else:
        return "NO"


print(check_dots(x1, y1, x2, y2))
