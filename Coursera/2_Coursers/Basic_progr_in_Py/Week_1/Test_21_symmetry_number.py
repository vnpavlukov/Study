num = int(input())


def checkSymmetry(num):
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10
    return int(a == d and b == c)


print(checkSymmetry(num))
