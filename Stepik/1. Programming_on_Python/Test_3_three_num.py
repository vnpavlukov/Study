a = int(input())
b = int(input())
c = int(input())

if c <= a >= b:
    print(a)
    if b >= c:
        print(c)
        print(b)
    else:
        print(b)
        print(c)
elif c <= b >= a:
    print(b)
    if c >= a:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

elif a <= c >= b:
    print(c)
    if a >= b:
        print(b)
        print(a)
    else:
        print(a)
        print(b)
