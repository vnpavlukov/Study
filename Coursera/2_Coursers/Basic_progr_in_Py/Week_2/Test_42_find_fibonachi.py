user_number = int(input())


def find_fibonacci(find_serial_number):
    if 0 < find_serial_number < 3:
        return 1
    prev_1, prev_2 = 1, 1
    serial_number = 2
    while serial_number < find_serial_number:
        serial_number += 1
        fibonacci = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = fibonacci
    return fibonacci


print(find_fibonacci(user_number))
