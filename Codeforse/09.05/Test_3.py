items = int(input())
numbers = []

for i in range(items):
    numbers.append(int(input()))


def check(num):
    answer = []
    mnoz = 1
    while num // 10:
        answer.append(int(str(num)[-1]) * mnoz)
        mnoz *= 10
        num = num // 10

    answer.append(num * mnoz)
    reverse = [i for i in answer if i != 0]
    print(len(reverse))
    for i in reverse:
        print(i, end=' ')
    print()


for num in numbers:
    check(num)
