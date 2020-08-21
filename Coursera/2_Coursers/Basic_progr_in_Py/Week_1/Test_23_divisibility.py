num_1 = int(input())
num_2 = int(input())


# values = {
#     10: 5,
#     100: 10,
#     4: 2,
#     9: 5,
#     31: 2
# }


def check_divisibility(num_1, num_2):
    return (['YES', 'NO'][int(bool(num_1 % num_2))])


# for numbers in values:
#     print(check_divisibility(numbers, values[numbers]))

print(check_divisibility(num_1, num_2))
