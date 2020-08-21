a = float(input())
n = float(input())


def rec(a, n):
    return (a ** 2) ** (n / 2) if n % 2 else (a * a ** (n - 1))


print(rec(a, n))
