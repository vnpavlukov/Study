a = int(input())
b = int(input())


def rec(a, b):
    if b != 0:
        b -= 1
        a += 1
        rec(a, b)
    else:
        print(a)


rec(a, b)
