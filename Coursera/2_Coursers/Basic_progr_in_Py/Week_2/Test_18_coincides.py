a = int(input())
b = int(input())
c = int(input())

if a == b or a == c or b == c:
    if a == b == c:
        print(3)
    else:
        print(2)
else:
    print(0)
