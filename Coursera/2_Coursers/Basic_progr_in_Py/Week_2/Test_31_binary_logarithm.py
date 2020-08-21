input_number = int(input())


def check_logarithm(check_number):
    i = 1
    degree = 0
    while i < check_number:
        i *= 2
        degree += 1
    return degree


print(check_logarithm(input_number))
