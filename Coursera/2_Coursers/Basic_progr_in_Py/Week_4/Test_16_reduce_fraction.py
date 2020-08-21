n = int(input())
m = int(input())


def gcd(a, b):
    if b != 0:
        if a > b:
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)
    return int(a)


def ReduceFraction(n, m):
    return int(n / gcd(n, m)), int(m / gcd(n, m))


print(*ReduceFraction(n, m))
