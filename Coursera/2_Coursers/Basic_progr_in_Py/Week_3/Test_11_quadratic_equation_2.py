a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D < 0:
    print(0)

elif a == 0 and b == 0 and c != 0:
    print(0)

elif a == 0 and b == 0 and c == 0:
    print(3)

elif a == 0:
    print(1, -c / b)

elif D == 0:
    print(1, - b / (2 * a))

elif D > 0:
    x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    if x_1 > x_2:
        print(2, x_2, x_1)
    else:
        print(2, x_1, x_2)
