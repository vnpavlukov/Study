items = int(input())
numbers = []

for i in range(items):
    numbers.append(int(input()))


def check(num):
    answer = []
    if len(str(num)) == 1:
        answer.append(num)
    elif len(str(num)) == 2:
        if num % 10 == 0:
            answer.append(num)
        else:
            answer.append(num // 10 * 10)
            answer.append(num % 10)

    elif len(str(num)) == 3:
        answer.append(num // 100 % 10 * 100)
        if num % 100 // 10 != 0:
            answer.append(num % 100 // 10 * 10)
        if num % 10 != 0:
            answer.append(num % 10)

    elif len(str(num)) == 4:
        answer.append(num // 1000 * 1000)
        if num // 100 % 10 != 0:
            answer.append(num // 100 % 10 * 100)
        if num % 100 // 10 != 0:
            answer.append(num % 100 // 10 * 10)
        if num % 10 != 0:
            answer.append(num % 10)
    else:
        answer.append(num)
    print(len(answer))
    for i in answer:
        print(i, end=' ')
    print()


for num in numbers:
    check(num)
