A = float(input())
B = float(input())
C = float(input())


def area_triangle(a, b, c):
    p = (a + b + c) / 2
    return pow(p * (p - a) * (p - b) * (p - c), 0.5)


print(area_triangle(A, B, C))
