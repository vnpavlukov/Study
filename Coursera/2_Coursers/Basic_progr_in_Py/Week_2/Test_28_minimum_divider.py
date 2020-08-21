checking_number = int(input())


def find_minimum_divider(number):
    i = 2
    while number % i != 0:
        i += 1
    return i


print(find_minimum_divider(checking_number))
