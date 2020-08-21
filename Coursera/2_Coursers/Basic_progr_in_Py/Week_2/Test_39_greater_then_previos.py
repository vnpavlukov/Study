number1 = int(input())
number_of_previous = 0
while number1 != 0:
    number2 = int(input())
    if number1 < number2:
        number_of_previous += 1
    number1 = number2

print(number_of_previous)
