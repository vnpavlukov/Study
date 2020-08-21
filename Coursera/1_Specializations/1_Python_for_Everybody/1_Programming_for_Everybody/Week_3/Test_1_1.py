def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(10):
    print(n, factorial(n + 1))

for n in range(1, 11):
    print(n ** 3)

for n in range(100):
    if n % 7 == 0:
        print(n)
