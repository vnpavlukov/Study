a = float(input())
b = float(input())


def gcd(a, b):
    if b != 0:
        if a > b:
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)
    return int(a)


print(gcd(a, b))
