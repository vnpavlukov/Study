def check_presents(first, second):
    steps = 0
    if 1 == len(set(first)) == len(set(second)):
        return steps

    length = len(first)
    steps = 0

    while min(first) != max(first) or min(second) != max(second):
        while True:
            delta = 0
            for i in range(length):
                if first[i] > min(first) and second[i] > min(second):
                    first[i] -= 1
                    second[i] -= 1
                    delta += 1
            if delta == 0:
                break
            else:
                steps += delta

        for i in range(length):
            if first[i] > min(first):
                first[i] -= 1
                steps += 1
                print(steps)
        for i in range(length):
            if second[i] > min(second):
                second[i] -= 1
                steps += 1
    return steps


count = int(input())
for i in range(count):
    _ = input()
    oranges = [int(i) for i in input().split()]
    candies = [int(i) for i in input().split()]
    print(check_presents(oranges, candies))
