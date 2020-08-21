def fib(n):
    f_1 = 1
    f_2 = 1
    i = 0
    while i < n - 2:
        fib_sum = f_1 + f_2
        f_1 = f_2 % 100
        f_2 = fib_sum % 100
        i = i + 1
    return f_2


def main():
    n = int(input())
    print(fib(n) % 10)


if __name__ == "__main__":
    main()
