input_number = int(input())


def check_degree_two(check_number):
    i = 1
    while i <= check_number:
        if i == check_number:
            return 'YES'
        i *= 2
    return 'NO'


print(check_degree_two(input_number))
