number = int(input())
maximum = number
while number != 0:
    if number > maximum:
        maximum = number
    number = int(input())
print(maximum)