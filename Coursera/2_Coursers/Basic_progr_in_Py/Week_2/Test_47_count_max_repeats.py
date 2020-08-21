current_number = int(input())
previous_number = 0
monotonic_length = 1
max_monotonic_length = 1

while current_number != 0:
    if current_number == previous_number:
        monotonic_length += 1
        if monotonic_length > max_monotonic_length:
            max_monotonic_length = monotonic_length
    if current_number != previous_number:
        monotonic_length = 1
    previous_number = current_number
    current_number = int(input())

print(max_monotonic_length)
