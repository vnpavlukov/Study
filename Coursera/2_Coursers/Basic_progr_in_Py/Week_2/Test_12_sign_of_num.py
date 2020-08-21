number = int(input())


def check_number(number):
    if number < 0:
        print(-1)
    elif number > 0:
        print(1)
    else:
        print(0)


check_number(number)
