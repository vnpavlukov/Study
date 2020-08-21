# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

x1 = 8
y1 = 9
x2 = 8
y2 = 8


def check_all_front_field(x_1, y_1, x_2, y_2):
    return y_2 > y_1 and abs(x_2 - x_1) <= y_2 - y_1


def check_inside_desk(x_1, y_1, x_2, y_2):
    return x_1 <= 8 and y_1 <= 8 and x_2 <= 8 and y_2 <= 8


def check_same_color(x_1, y_1, x_2, y_2):
    return (x_1 + y_1) % 2 == (x_2 + y_2) % 2


def check_move(x_1, y_1, x_2, y_2):
    if check_all_front_field(x_1, y_1, x_2, y_2) == \
            check_inside_desk(x_1, y_1, x_2, y_2) == \
            check_same_color(x_1, y_1, x_2, y_2) == True:
        return 'YES'
    else:
        return 'NO'


print(check_move(x1, y1, x2, y2))
