number = int(input())
sum_of_numbers = 0
while number != 0:
    if number % 2 == 0:
        sum_of_numbers += 1
    number = int(input())

print(sum_of_numbers)
