n = float(input())
x = float(input())
a = float(input())
P_x = a
i = 1

while i <= n:
    a = float(input())
    P_x = P_x * x + a
    i += 1

print(P_x)
