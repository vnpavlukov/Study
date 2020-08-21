limitation = int(input())
max_num = 1
b = 1

while max_num <= limitation:
    print(b ** 2, end=' ')
    b += 1
    max_num = b ** 2
