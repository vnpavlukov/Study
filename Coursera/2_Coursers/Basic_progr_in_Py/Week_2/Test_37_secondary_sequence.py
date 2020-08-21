number = int(input())
sum_of_numbers = 0
count_numbers = 0
while number != 0:
    sum_of_numbers += number
    number = int(input())
    count_numbers += 1

print(float(sum_of_numbers / count_numbers))
