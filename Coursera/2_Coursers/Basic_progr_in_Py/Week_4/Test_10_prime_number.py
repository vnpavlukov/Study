n = int(input())


def IsPrime(n):
    i = 2
    if i == n:
        return True
    while n % i != 0:
        if i > n ** 0.5:
            return True
        i += 1
    return False


if IsPrime(n):
    print('YES')
else:
    print('NO')
