a = float(input())
n = int(input())


def power(a, n):
    i = 1
    uns = a
    if n == 0:
        return 1
    elif n < 0:
        n *= -1
        while i < n:
            uns *= a
            i += 1
        return 1 / uns
    else:
        while i < n:
            uns *= a
            i += 1
        return uns


print(power(a, n))
