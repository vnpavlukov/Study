a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == b == c == d == e == f == 0:
    print(5)
elif a == b == c == d == 0 and (e != f == 0):
    print(0)
elif a * d == c * b and a * f != c * e:
    print(0)
elif a == b == 0 and e != 0:
    print(0)
elif c == d == 0 and f != 0:
    print(0)
elif a == c == 0 and b * f != d * e:
    print(0)
elif b == d == 0 and a * f != c * e:
    print(0)
elif a * d == b * c and a * f == c * e:
    if b == d == 0:
        if c != 0 and a != 0:
            print(3, e / a)
        elif c == 0:
            if f == 0:
                print(3, e / a)
        elif a == 0:
            if e == 0:
                print(3, f / c)
    elif a == c == 0:
        if d != 0:
            print(4, f / d)
        elif b != 0:
            print(4, e / b)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    x = (e * d - b * f) / (d * a - c * b)
    y = (f * a - c * e) / (d * a - c * b)
    print(2, int(x), int(y))
