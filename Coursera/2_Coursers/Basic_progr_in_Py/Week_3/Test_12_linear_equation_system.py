a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (d * a - c * b) != 0:
    x = (e * d - b * f) / (d * a - c * b)
    y = (f * a - c * e) / (d * a - c * b)
else:
    x = 0
    y = 0

print(float(x), float(y))
