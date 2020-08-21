items = int(input())
numbers = []

for i in range(items):
    numbers.append(int(input()))


def check(num):
    if len(str(num)) == 1:
        print(1)
        print(num)

    elif len(str(num)) == 2:
        if num % 10 == 0:
            print(1)
            print(num)
        else:
            print(2)
            print(num // 10 * 10, num % 10)

    elif len(str(num)) == 3:
        if num % 10 == num % 100 == 0:
            print(1)
            print(num)
        elif num % 10 == 0:
            print(2)
            print(num // 100 * 100, num % 100)
        elif num // 10 % 10 == 0:
            print(2)
            print(num // 100 * 100, num % 100)
        else:
            print(3)
            print(num // 100 * 100, num // 10 % 10 * 10, num % 10)

    elif len(str(num)) == 4:
        if num // 100 % 10 == num % 100 // 10 == num % 10 == 0:
            print(1)
            print(num)
        elif num % 100 // 10 == num % 10 == 0:
            print(2)
            print(num // 1000 * 1000, num // 100 % 10 * 100)
        elif num % 10 == num // 100 % 10 == 0:
            print(2)
            print(num // 1000 * 1000, num % 100 // 10 * 10)
        elif num % 10 == 0:  # 5670
            print(3)
            print(num // 1000 * 1000, num // 100 % 10 * 100,
                  num % 100 // 10 * 10)
        elif num % 100 // 10 == 0 and num // 100 % 10 != 0 and num % 10 != 0:
            print(3)
            print(num // 1000 * 1000, num // 100 % 10 * 100, num % 10)
        elif num // 100 % 10 == num % 100 // 10 == 0:
            print(2)
            print(num // 1000 * 1000, num % 10)
        else:
            print(4)
            print(num // 1000 * 1000, num // 100 % 10 * 100,
                  num % 100 // 10 * 10, num % 10)
    else:
        print(1)
        print(num)


for num in numbers:
    check(num)
