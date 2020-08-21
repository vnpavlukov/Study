num = int(input())
num_even = num % 2 == 0
print(num_even)



while first_number != 0:
    if first_number > maximum_repeat and first_number == second_number:
        count = 1
    if first_number >= maximum_repeat and first_number == second_number:
        maximum_repeat = first_number
        count += 1
    second_number = first_number
    first_number = int(input())