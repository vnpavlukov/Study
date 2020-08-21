a = int(input())
b = int(input())

if a % 3 != 0:
    a += 1
    if a % 3 != 0:
        a += 1

sum = 0
n = 0

for i in range(a, b + 1, 3):
    n += 1
    sum += i

print(sum / n)
