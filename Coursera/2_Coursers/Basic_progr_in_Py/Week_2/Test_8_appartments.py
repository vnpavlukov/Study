appart_1 = int(input())
appart_2 = int(input())


def check_apartments(num1, num2):
    if num1 == 1:
        print('YES')
    elif num2 % (num2 - num1 + 1) == 0:
        print('YES')
    else:
        print('NO')


check_apartments(appart_1, appart_2)
