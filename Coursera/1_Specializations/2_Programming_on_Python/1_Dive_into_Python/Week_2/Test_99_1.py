x = 0


def f(n):
    # x = 0
    global x
    while n != 1:
        x += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    return x


print(f(f(f(f(f(f(f(674))))))))
print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))