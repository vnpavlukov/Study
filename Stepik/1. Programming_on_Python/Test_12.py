a, b = input().split()
# a, b = (int(i) for i in input().split())
a = int(a)
b = int(b)

sum = 0

# 1
for i in range(a, b + 1):
    if i % 2 == 1:
        sum += i
print(sum)

# 2
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    sum += i
print(sum)


