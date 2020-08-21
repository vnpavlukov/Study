x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

white = 2 + n * x, 2 + n * y
black = n * x, n * y


if a < b:
    if b < c:
        print(c)
    else:
        print(b)
elif a < c:
    print(c)
else:
    print(a)
