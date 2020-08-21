user_fibonacci = int(input())


def find_sn_fibonacci(input_number):
    if input_number == 1:
        return 1
    if input_number == 2:
        return 3
    prev_1, prev_2 = 1, 1
    fibonacci = prev_1 + prev_2
    serial_number = 2
    while fibonacci < input_number:
        serial_number += 1
        fibonacci = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = fibonacci
    if input_number == fibonacci:
        return serial_number
    else:
        return -1


print(find_sn_fibonacci(user_fibonacci))
