count = int(input())


def check(num):
    if len(num) == 1:
        return 'YES'
    if len(set(num)) == 1:
        return 'YES'
    n = []
    for i in range(len(num)):
        try:
            if num[i] == num[i + 1] or num[i + 1] - num[i] <= 1:
                continue
            n.append(num[i])
        except IndexError:
            continue
    return "NO" if n else "YES"


for i in range(count):
    _ = input()
    numbers = [int(i) for i in input().split()]
    print(check(numbers))
