sum = 0
square = 0

while True:
    input_num = int(input())
    sum += input_num
    square += (input_num ** 2)
    if sum == 0:
        break
print(square)
